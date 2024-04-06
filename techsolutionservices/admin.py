from django.contrib import admin
from techsolutionservices.models import techservices


class techservicesAdmin(admin.ModelAdmin):
    List_display = (
        "techservices_icon",
        "techservices_title",
        "techservices_des",
    )


admin.site.register(techservices, techservicesAdmin)
