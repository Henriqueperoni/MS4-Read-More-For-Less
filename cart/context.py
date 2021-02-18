from django.shortcuts import get_object_or_404
from pricing.models import Pricing


def cart_contents(request):

    cart_items = []
    total = 0
    plan_counter = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        if plan_counter < 1:
            plan_counter += 1
            plan = get_object_or_404(Pricing, pk=item_id)
            total = plan.price
            cart_items.append({
                'item_id': item_id,
                'plan': plan,
            })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
