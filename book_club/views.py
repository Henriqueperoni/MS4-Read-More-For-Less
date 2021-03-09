from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import BookReview, ReviewComment
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
    review_comments = ReviewComment.objects.all()

    context = {
        'review': review,
        'review_comments': review_comments,
    }

    return render(request, 'book_club/view_review.html', context)


def create_review(request):
    """  A view to return the create_review template and CreateReview form. """

    if request.method == 'POST':
        create_review_form = BookReview(
            user=request.user,
            book_name=request.POST.get('book_name'),
            book_author=request.POST.get('book_author'),
            book_review=request.POST.get('book_review'),
            image_url=request.POST.get('image_url'),
        )

        create_review_form.save()
        messages.success(request, "Review created successfully")
        return redirect('book_club')

    context = {
        'form': CreateReviewForm
    }

    return render(request, 'book_club/create_review.html', context)
