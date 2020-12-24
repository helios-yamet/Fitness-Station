from django import forms
from .models import Order
from datetime import datetime


year = int(datetime.now().strftime("%Y"))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False


class MakePaymentForm(forms.Form):
    """
    Input for Stripe Payment Collection
    Default Expiration Year Range to current Year
    Create month& year variables attach year range.
    Create credit card form field and expiry stripe variables.
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(year, year + 20)]

    credit_card_number = forms.CharField(label='Credit Card Number',
                                         required=False)
    ccv = forms.CharField(label="Security Code", required=False)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
