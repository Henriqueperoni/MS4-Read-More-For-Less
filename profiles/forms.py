from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'genres': 'Genres',
            'favorite_authors': 'Let us know more about your favorite authors',
            'favorite_books': (
                'Books you enjoy reading to help us send good books for you'),
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_post_code': ' Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields['favorite_authors'].widget.attrs['rows'] = 5
            self.fields['favorite_books'].widget.attrs['rows'] = 5
            self.fields[field].label = False
