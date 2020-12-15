from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    A review linked to the user that created it and the product being reviewed.
    """

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="review",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="review",
    )
    review_content = models.TextField(blank=True, null=True, default="")
