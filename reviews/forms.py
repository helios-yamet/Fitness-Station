from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form linked to review model to create or edit a review.
    """

    class Meta:
        model = Review
        fields = ["review_content"]
        widgets = {
            "review_content": forms.Textarea(
                attrs={
                    "disabled": True,
                    "class": "review-form-textarea",
                    "rows": 10,
                    "placeholder": "Minimum 15 characters",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["review_content"].label = False
        self.fields["review_content"].widget.attrs["aria-label"] = "review content"
