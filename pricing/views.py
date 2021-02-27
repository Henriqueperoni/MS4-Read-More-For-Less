from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def add_plan(request):
    """ Add a product to the store """
    if request.method == "POST":
        form = PricingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New plan successfully added')
            return redirect(reverse('add_plan'))
        else:
            messages.error(
                request, 'Failed to add plan. Please ensure the form is valid')
    else:
        form = PricingForm()

    template = 'pricing/add_plan.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_plan(request, pricing_id):
    plan = get_object_or_404(Pricing, pk=pricing_id)

    if request.method == 'POST':
        form = PricingForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, f'{plan.name} successfully updated!')
            return redirect(reverse('pricing'))
        else:
            messages.error(request, 'Failed to update plan. \
                Please ensure the for is valid')
    else:
        form = PricingForm(instance=plan)
        messages.info(request, f'You are editing {plan.name}')

    template = 'pricing/edit_plan.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)
