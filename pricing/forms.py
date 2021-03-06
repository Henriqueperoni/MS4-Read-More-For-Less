from django import forms
from .models import Pricing


class PricingForm(forms.ModelForm):

    class Meta:
        model = Pricing
        fields = ('name', 'description', 'price', 'frequency')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
