from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pricing
from profiles.models import UserProfile


from .forms import PricingForm, BookPreferencesForm

# Create your views here.


def plans_pricing(request):
    """ A view to show all the plans available """

    pricing = Pricing.objects.all().order_by('price')

    context = {
        'pricing': pricing,
    }

    return render(request, 'pricing/pricing.html', context)


def plan_detail(request, pricing_id):
    """ A view to show individual product details """

    pricing = get_object_or_404(Pricing, pk=pricing_id)

    user = get_object_or_404(UserProfile, pk=request.user.id)
    print(user)

    if request.method == 'POST':
        form_data = {
                'genres': request.POST['genres'],
                'favorite_authors': request.POST['favorite_authors'],
                'favorite_books': request.POST['favorite_books'],
            }

        book_preferences_form = BookPreferencesForm(form_data)
        if book_preferences_form.is_valid():
            book_preferences = book_preferences_form.save(commit=False)
            book_preferences.user = request.user
            book_preferences.save()
            messages.success(
                request, 'Book Preferences successfully save')
    else:
        book_preferences_form = BookPreferencesForm(instance=user)

    context = {
        'pricing': pricing,
        'book_preferences_form': book_preferences_form,
    }

    return render(request, 'pricing/plan_detail.html', context)


# def book_preferences(request):

#     if request.method == 'POST':
#         form = BookPreferencesForm(request.POST)
#         if form.is_valid():
#             form.save()

#     form = BookPreferencesForm()
#     template = 'pricing/plan_detail.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)


@login_required
def add_plan(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def edit_plan(request, pricing_id):
    """ Edit a plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_plan(request, pricing_id):
    """ Delete a plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that.')
        return redirect(reverse('home'))

    plan = get_object_or_404(Pricing, pk=pricing_id)
    plan.delete()
    messages.success(request, f'{plan.name} deleted')
    return redirect(reverse('pricing'))
