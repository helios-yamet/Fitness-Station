from django.db import models
from products.models import Product
from django.utils import timezone


class Review(models.Model,):
    """
    This model will store a review text, reviewer and
    date of submission to a product.
    """
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    review_text = models.CharField(max_length=800, blank=False, default='')
    reviewer = models.CharField(max_length=100, blank=False, default='')
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.reviewer
