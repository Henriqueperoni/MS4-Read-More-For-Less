from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware

from .forms import Order, OrderForm
from cart.context import cart_contents
from pricing.models import Pricing
from .models import OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        start_date = make_aware(datetime.now())
        end_date = start_date + relativedelta(years=1)

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'post_code': request.POST['post_code'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.start_date = start_date
            order.end_date = end_date
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for item_id, quantity in cart.items():
                plan = get_object_or_404(Pricing, pk=item_id)
                total += quantity * plan.price
                total = plan.price
                order_line_item = OrderLineItem(
                    order=order,
                    plan=plan,
                    quantity=quantity,
                )
                order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('pricing'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'post_code': profile.default_post_code,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle succesfull checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    end_date = datetime.strftime(order.end_date, '%d %B %Y')

    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'genres': profile.genres,
            'favorite_authors': profile.favorite_authors,
            'favorite_books': profile.favorite_books,
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_post_code': order.post_code,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order succesfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'end_date': end_date,
    }

    return render(request, template, context)


def check_active_plan():
    """ Function to check if user still have a valid plan """
    date = make_aware(datetime.now())
    end_dates = Order.objects.filter(end_date__lte=date)
    end_dates.delete()
