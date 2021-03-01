from django.db import models
from django.contrib.auth.models import User

# Create your models here.

frequency_types = [
    ('monthly', 'Monthly'),
    ('biannual', 'Biannual'),
    ('annually', 'Annually')
]

genres = {
    ('mindset', 'Mindset'),
    ('business', 'Business'),
    ('biography', 'Biography'),
    ('romance', 'Romance'),
    ('crime', 'Crime'),
    ('horror', 'Horror'),
    ('children', 'Children'),
}


class Pricing(models.Model):

    class Meta:
        verbose_name_plural = 'Pricing'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    introduction = models.TextField(max_length=600)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.CharField(max_length=20, choices=frequency_types)

    def __str__(self):
        return self.name


class BookPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.CharField(
        max_length=20, choices=genres, null=True, blank=True)
    favorite_authors = models.TextField(max_length=100, null=True, blank=True)
    favorite_books = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user
