from django.db import models

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
    ('children', 'Children')
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
