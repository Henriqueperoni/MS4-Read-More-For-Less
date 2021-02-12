from django.conf import settings
from django.shortcuts import get_object_or_404
from pricing.models import Pricing


def cart_contents(request):

    cart_items = []
    total = 0
    plan_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        if plan_count < 1:
            plan_count += 1
            plan = get_object_or_404(Pricing, pk=item_id)
            total += quantity * plan.price
            cart_items.append({
                'item_id': item_id,
                'plan': plan,
            })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
