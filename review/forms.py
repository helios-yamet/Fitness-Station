from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Create review form class model
    """

    class Meta:
        """
        Call model& add fields
        """
        model = Review
        fields = ('name', 'review_text', 'date')
