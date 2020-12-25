from django.db import models
from products.models import Product
from django.utils import timezone


class Review(models.Model,):
    """
    This model will store a review text, username
    and review submission date.
    Create product review variable& add field requirements.
    Return product model.
    """
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    review_text = models.TextField(max_length=200, blank=False, default='')
    name = models.CharField(max_length=50, blank=False, default='')
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
