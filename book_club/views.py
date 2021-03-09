from django.shortcuts import render, get_object_or_404

from .models import BookReview
from .forms import CreateReviewForm


def book_club(request):
    """ A view to return the book club page with book reviews. """
    reviews = BookReview.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'book_club/book_club.html', context)


def view_review(request, review_id):
    """
    A view to return a book review that enable user to add comments to it.
    """
    review = get_object_or_404(BookReview, pk=review_id)
    print(f'REVIEW: {review}')

    context = {
        'review': review,
    }

    return render(request, 'book_club/view_review.html', context)


def create_review(request):
    """  A view to return the create_review template and CreateReview form. """

    context = {
        'form': CreateReviewForm
    }

    return render(request, 'book_club/create_review.html', context)
