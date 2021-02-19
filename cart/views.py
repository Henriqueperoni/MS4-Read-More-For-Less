from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from pricing.models import Pricing
# Create your views here.


def view_cart(request):
    """ A view that renders the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a pricing plan to the shopping cart"""

    plan = get_object_or_404(Pricing, pk=item_id)
    quantity = 1
    cart = request.session.get('cart', {})

    if cart.items():
        messages.error(request, 'You already have a plan in your cart')
        print(len(cart))

    if len(cart) < 1:
        cart[item_id] = cart.get(item_id, quantity)
        messages.success(
            request, f"Successfully added {plan.frequency.lower()} \
                {plan.name}'s plan to cart")

    request.session['cart'] = cart
    return redirect('pricing')


def clear_cart(request):
    """ Remove plan from the cart """

    cart = request.session.get('cart', {})

    cart.clear()
    messages.success(request, 'Your cart has successfully been cleared')

    request.session['cart'] = cart
    return redirect('pricing')
