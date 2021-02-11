from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0



    context ={
        'cart_items': cart_items,
        'total': total,
    }

    return context