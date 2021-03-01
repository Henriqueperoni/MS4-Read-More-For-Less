from django import forms
from .models import Pricing, BookPreferences


class PricingForm(forms.ModelForm):

    class Meta:
        model = Pricing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BookPreferencesForm(forms.ModelForm):
    class Meta:
        model = BookPreferences
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
