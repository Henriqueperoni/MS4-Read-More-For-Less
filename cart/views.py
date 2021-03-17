from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from pricing.models import Pricing
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def view_cart(request):
    """ A view that renders the cart content page """
    user = get_object_or_404(UserProfile, user=request.user)
    book_preferences_form = UserProfileForm(instance=user)

    if request.method == 'POST':
        book_preferences_form = (
            UserProfileForm(request.POST, instance=user))
        if book_preferences_form.is_valid():
            book_preferences_form.save()
            messages.success(
                request, 'Book Preferences information updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please, ensure the form is valid')
    else:
        book_preferences_form = UserProfileForm(instance=user)

    context = {
        'book_preferences_form': book_preferences_form,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """ Add a pricing plan to the shopping cart"""
    user = get_object_or_404(UserProfile, user=request.user)
    orders = user.orders.all()
    plan = get_object_or_404(Pricing, pk=item_id)
    quantity = 1
    cart = request.session.get('cart', {})

    if request.user.is_authenticated:
        if len(orders) >= 1:
            messages.error(request, 'You already have a plan')
            return redirect(reverse('pricing'))
        else:
            if cart.items():
                messages.error(request, 'You already have a plan in your cart')

            if len(cart) < 1:
                cart[item_id] = cart.get(item_id, quantity)
                messages.success(
                    request, f"Successfully added {plan.frequency.lower()} \
                        {plan.name}'s plan to cart")
                request.session['cart'] = cart
                return redirect(reverse('view_cart'))
    else:
        messages.error(
            request, 'You must be logged in to add a plan to the cart')

    request.session['cart'] = cart
    return redirect('pricing')


def clear_cart(request):
    """ Remove plan from the cart """

    cart = request.session.get('cart', {})

    cart.clear()
    messages.success(request, 'Your cart has successfully been cleared')

    request.session['cart'] = cart
    return redirect('pricing')
