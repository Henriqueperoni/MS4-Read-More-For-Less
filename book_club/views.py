from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BookReview, ReviewComment
from .forms import CreateReviewForm, CreateCommentForm


@login_required
def book_club(request):
    """ A view to return the book club page with book reviews. """
    reviews = BookReview.objects.all().order_by('date_posted')

    context = {
        'reviews': reviews,
    }

    return render(request, 'book_club/book_club.html', context)


@login_required
def view_review(request, review_id):
    """
    A view to return a book review that enable user to add comments to it.
    """
    review = get_object_or_404(BookReview, pk=review_id)
    review_comments = ReviewComment.objects.filter(
        review_id=review_id).order_by('-date_commented')

    if request.method == 'POST':
        create_comment_form = ReviewComment(
            comment_text=request.POST.get('comment_text'),
            user=request.user,
            review=review
        )
        create_comment_form.save()
        messages.success(request, 'Comment successfully added')
        return redirect('view_review', review_id)

    context = {
        'review': review,
        'review_comments': review_comments,
        'form': CreateCommentForm,
    }

    return render(request, 'book_club/view_review.html', context)


@login_required
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


@login_required
def edit_review(request, review_id):
    """ A view to allows the user edit their reviews """
    review = get_object_or_404(BookReview, pk=review_id)

    if request.user != review.user:
        messages.error(
            request, 'Sorry, only the creator of this review can edit it.')
        return redirect(reverse('book_club'))

    if request.method == 'POST':
        edit_review_form = CreateReviewForm(request.POST, instance=review)
        if edit_review_form.is_valid():
            edit_review_form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('view_review', review_id)
        else:
            messages.error(request, 'Failed to update Review. \
                Please, ensure the for is valid')
    else:
        edit_review_form = CreateReviewForm(instance=review)
        messages.info(request, f'You are editing {review.book_name}')

    context = {
        'form': edit_review_form,
        'review': review
    }

    return render(request, 'book_club/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ A view to allows the user delete their reviews """
    review = get_object_or_404(BookReview, pk=review_id)

    if request.user == review.user or request.user.is_superuser:
        review.delete()
        messages.success(request, f'{review.book_name} deleted')
    else:
        messages.error(
            request, 'Sorry, only the creator of this review can do that.')
        return redirect(reverse('book_club'))

    return redirect(reverse('book_club'))
