from django.db import models

# Create your models here.

frequency_types = [
    ('monthly', 'Monthly'),
    ('biannual', 'Biannual'),
    ('yearly', 'Yearly')
]


class Pricing(models.Model):

    class Meta:
        verbose_name_plural = 'Pricing'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.CharField(max_length=20, choices=frequency_types)

    def __str__(self):
        return self.name
