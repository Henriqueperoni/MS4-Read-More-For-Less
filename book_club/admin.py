from django.contrib import admin
from .models import BookReview, ReviewComment


class ReviewCommentAdminInline(admin.TabularInline):
    model = ReviewComment
    readonly_fields = ('user', 'comment_text', 'review', 'date_commented',)
    ordering = ('-date_commented',)


class BookReviewAdmin(admin.ModelAdmin):
    inlines = (ReviewCommentAdminInline,)

    fields = ('user', 'book_name', 'book_author',
              'book_review', 'image_url', 'date_posted',)
    ordering = ('-date_posted',)


admin.site.register(BookReview, BookReviewAdmin)
