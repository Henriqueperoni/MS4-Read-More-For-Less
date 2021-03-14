from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ A view to return the contact page """
    form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
