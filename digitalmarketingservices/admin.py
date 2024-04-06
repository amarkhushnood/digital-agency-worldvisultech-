from django.contrib import admin
from digitalmarketingservices.models import digitalservices


class digitalservicesAdmin(admin.ModelAdmin):
    List_display = (
        "digitalservices_icon",
        "digitalservices_title",
        "digitalservices_des",
    )


admin.site.register(digitalservices, digitalservicesAdmin)
