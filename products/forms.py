from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Create product models& attach add product fields.
    Create image label, add image field to the label.
    apply custom file widget, user can select image file.
    """
    class Meta:
        model = Product
        fields = "__all__"

        image = forms.ImageField(
            label="Image", required=False, widget=CustomClearableFileInput
        )

        def __init__(self, *args, **kwargs):
            """
            Define init and pass two arguments.
            Get category, attach all category objects.
            Find product category in available categories.
            Return category friendly name field.
            """
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            friendly_names = [(c.id, c.get_friendly_name())
                              for c in categories]

            self.fields["category"].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs["class"] = "border-warning rounded-0"
