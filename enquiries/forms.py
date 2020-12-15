from django import forms

# our new form


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=20, min_length=5,
                                required=True)
    contact_email = forms.EmailField(max_length=20, min_length=5,
                                     required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea, max_length=500, min_length=5,
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "contact_email": "Contact Email",
            "content": "Content"
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
                self.fields[field].widget.attrs["class"] = "stripe-style-input"
                self.fields[field].label = False
