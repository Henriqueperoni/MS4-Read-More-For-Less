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
        placeholders = {
            'genres': 'Genre',
            'favorite_authors': 'Favorite Authors',
            'favorite_books': 'Favorite Books',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
