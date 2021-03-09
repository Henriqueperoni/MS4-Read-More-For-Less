from django.contrib import admin
from .models import BookReview, ReviewComment


admin.site.register(BookReview)
admin.site.register(ReviewComment)
