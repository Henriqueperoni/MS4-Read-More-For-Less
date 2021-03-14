from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
import os

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        customer_email = request.POST.get('email')
        customer_query = request.POST.get('comments')
        if form.is_valid():
            form.save()

            # Send Email
            send_mail(
                'Read More For Less - New Contact Form',
                customer_query,
                [customer_email],
                os.environ.get('EMAIL'),
            )
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
