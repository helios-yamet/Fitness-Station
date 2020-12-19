from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create contact form model,
    attach message fields to contact model.
    """

    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message')
