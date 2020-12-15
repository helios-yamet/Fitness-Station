from django.contrib import admin
from .models import Enquiries


class EnquiriesAdmin(admin.ModelAdmin):
    """
    Display and modify enquiries in admin panel.
    """

    list_display = (
        "full_name",
        "contact_email",
        "content",
    )


admin.site.register(Enquiries, EnquiriesAdmin)
