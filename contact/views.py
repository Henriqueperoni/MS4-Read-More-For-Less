from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Mail sent. We will be in touch soon.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Contact request failed. Please, ensure the form is valid!')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
