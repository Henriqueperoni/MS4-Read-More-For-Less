from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import Order, OrderForm
from cart.context import cart_contents
from pricing.models import Pricing
from .models import OrderLineItem

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.session.get('full_name', {}),
            'email': request.session.get('email', {}),
            'phone_number': request.session.get('phone_number', {}),
            'country': request.session.get('country', {}),
            'post_code': request.session.get('post_code', {}),
            'town_or_city': request.session.get('town_or_city', {}),
            'street_address1': request.session.get('street_address1', {}),
            'street_address2': request.session.get('street_address2', {}),
            'county': request.session.get('county', {}),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for item_id, quantity in cart.items():
                plan = get_object_or_404(Pricing, pk=item_id)
                total += quantity . plan.price
                total = plan.price
                order_line_item = OrderLineItem(
                    order=order,
                    plan=plan,
                    quantity=quantity,
                )
                order_line_item.save()

        request.session['save_info'] = 'save-info' in request.POST
        return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public is missing.')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle succesfull checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order succesfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')

    if 'cart' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
