from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
    if request.method == "POST":
        form = PricingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New plan successfully added')
            return redirect(reverse('add_pricing'))
        else:
            messages.error(
                request, 'Failed to add plan. Please ensure the form is valid')
    else:
        form = PricingForm()

    template = 'pricing/add_pricing.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
