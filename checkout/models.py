import uuid

from django.db import models
from pricing.models import Pricing

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_adrdress1 = models.CharField(max_length=80, null=False, blank=False)
    street_adrdress2 = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a radon, unique oder number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE)
    plan = models.ForeignKey(
        Pricing, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return f'Plan {self.plan.price} on order {self.order.order_number}'
