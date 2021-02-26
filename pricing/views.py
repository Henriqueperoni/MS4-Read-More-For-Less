from django.shortcuts import render
from .models import Pricing

from .forms import PricingForm

# Create your views here.


def plans_pricing(request):
    """ A view to show all the plans available """
    pricing = Pricing.objects.all().order_by('price')

    context = {
        'pricing': pricing,
    }

    return render(request, 'pricing/pricing.html', context)


def add_pricing(request):
    """ Add a product to the store """
    form = PricingForm()
    template = 'pricing/add_pricing.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
