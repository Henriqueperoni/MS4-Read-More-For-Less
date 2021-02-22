from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51INjtFIjHLDaRybQ5iABuBVzX9zc58FXMuDp3p2l0vuCpMq00Zs1yKvfqxsFPJlTc8jbMWM4syAw4LDmgEOmpJsM00vMpX3PI8',
    }

    return render(request, template, context)