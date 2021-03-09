from django.shortcuts import render

from .models import BookReview


def book_club(request):
    """ A view to return the book club page with book reviews """
    reviews = BookReview.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'book_club/book_club.html', context)
