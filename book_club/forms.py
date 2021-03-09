from django import forms
from .models import BookReview, ReviewComment


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        fields = ('book_name', 'book_author', 'image_url', 'book_review',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus no first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'book_name': 'Book Name',
            'book_author': 'Book Author',
            'image_url': ' Image URL',
            'book_review': 'Book Review',
        }

        self.fields['book_review'].widget.attrs['rows'] = 5

        self.fields['book_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = ReviewComment
        fields = ('comment_text',)

    comment_text = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'stripe-style-input',
            'placeholder': 'Add your Comment Details',
        })
    )
