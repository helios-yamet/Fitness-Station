from django import forms

# our new form


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=20, min_length=5, required=True)
    contact_email = forms.EmailField(max_length=20,
                                     min_length=5, required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea, max_length=500, min_length=5
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What would you like to know?"
