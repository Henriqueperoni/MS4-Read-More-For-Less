from django.shortcuts import render, redirect
from django.contrib import messages

from pricing.models import Pricing
# Create your views here.


def view_cart(request):
    """ A view that renders the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a pricing plan to the shopping cart"""

    plan = Pricing.objects.get(pk=item_id)
    quantity = 1
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, quantity)

    messages.success(
        request, f"Successfully added {plan.name}'s plan to cart")
    request.session['cart'] = cart
    return redirect('pricing')


def clear_cart(request):
    """ Remove plan from the cart """

    cart = request.session.get('cart', {})

    cart.clear()

    request.session['cart'] = cart
    return redirect('pricing')
