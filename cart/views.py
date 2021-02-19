from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def view_cart(request):
    """ A view that renders the cart content page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a pricing plan to the shopping cart"""

    quantity = 1
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, quantity)

    messages.success(request, 'Added to the cart')
    request.session['cart'] = cart
    return redirect('pricing')


def clear_cart(request):
    """ Remove plan from the cart """

    cart = request.session.get('cart', {})

    cart.clear()

    request.session['cart'] = cart
    return redirect('pricing')
