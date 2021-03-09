from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BookReview(models.Model):
    """
    A model to save and display book reviews
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50, null=False, blank=False)
    book_author = models.CharField(max_length=50, null=False, blank=False)
    book_review = models.TextField(max_length=1500, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_name
