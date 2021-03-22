from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page and send emails alerting
    the admin about a new Contact Form been submitted. """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        customer_query = request.POST.get('comments')
        if form.is_valid():
            form.save()

            send_mail(
                'Read More For Less - New Contact Form',
                'You have a new contact form available to you on '
                'Read More For Less. \n\n\nCustomer Query:'
                f'\n\n{customer_query}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
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
