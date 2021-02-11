from django.shortcuts import render
from .models import Pricing

# Create your views here.


def plans_pricing(request):
    """ A view to show all the plans available """
    pricing = Pricing.objects.all().order_by('price')

    context = {
        'pricing': pricing,
    }

    return render(request, 'pricing/pricing.html', context)
