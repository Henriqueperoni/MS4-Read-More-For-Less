from django.db import models

# Create your models here.


class Pricing(models.Model):

    class Meta:
        verbose_name_plural = 'Pricing'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.CharField(max_length=15)

    def __str__(self):
        return self.name
