from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from pricing.models import Pricing
from profiles.models import UserProfile


def view_cart(request):
    """ A view that renders the cart content page """
    return render(request, 'cart/cart.html')


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
            return redirect(reverse('home'))
        else:
            if cart.items():
                messages.error(request, 'You already have a plan in your cart')

            if len(cart) < 1:
                cart[item_id] = cart.get(item_id, quantity)
                messages.success(
                    request, f"Successfully added {plan.frequency.lower()} \
                        {plan.name}'s plan to cart")
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
