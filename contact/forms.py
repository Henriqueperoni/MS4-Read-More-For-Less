from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_reason', 'name', 'email',
                  'comments')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus no first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_reason': '',
            'name': 'Enter your Name',
            'email': 'Enter you Email',
            'comments': 'Let us know how we can best assist you',
        }

        self.fields['contact_reason'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
