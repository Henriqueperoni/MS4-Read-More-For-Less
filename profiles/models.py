from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

genres = [
    ('random_genres', 'Random Genres'),
    ('art', 'Art'),
    ('biography', 'Biography'),
    ('business', 'Business'),
    ('children', 'Children')
    ('crime', 'Crime'),
    ('health', 'Health'),
    ('romance', 'Romance'),
    ('mindset', 'Mindset'),
    ('horror', 'Horror'),
]


class UserProfile(models.Model):
    """
    A user profile model for maintaning default information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.CharField(
        max_length=20, choices=genres, blank=False, default='random_genres')
    favorite_authors = models.TextField(max_length=100, blank=True)
    favorite_books = models.TextField(max_length=100, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_post_code = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=40, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
    instance.userprofile.save()
