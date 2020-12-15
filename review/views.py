from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    """
    Display and modify reviews in admin panel.
    """

    list_display = (
        "user_profile",
        "product",
    )


admin.site.register(Review, ReviewsAdmin)
