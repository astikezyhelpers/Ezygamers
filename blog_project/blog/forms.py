from django import forms
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=10, required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        message = cleaned_data.get('message')

        if not email and not phone_number:
            raise ValidationError("Either email or phone number must be provided.")
        
        if phone_number and not re.match(r'^\d{10}$', phone_number):
            raise ValidationError("Phone number must be exactly 10 digits.")
        
        if message and re.search(r'[^\w\s]', message):
            raise ValidationError("Message should not contain special characters.")

        return cleaned_data
