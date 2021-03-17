from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.views import check_active_plan
from checkout.models import Order
from book_club.models import BookReview


@login_required
def profile(request):
    """ Display the user's profile. """
    # Check if user has a valid plan
    check_active_plan()

    profile = get_object_or_404(UserProfile, user=request.user)
    book_reviews = BookReview.objects.order_by('-date_posted')
    my_reviews = book_reviews.filter(user__exact=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Information updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please, ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'my_reviews': my_reviews,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
