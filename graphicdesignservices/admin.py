from django.contrib import admin
from graphicdesignservices.models import graphicservices


class graphicservicesAdmin(admin.ModelAdmin):
    List_display = (
        "graphicservices_icon",
        "graphicservices_title",
        "graphicservices_des",
    )


admin.site.register(graphicservices, graphicservicesAdmin)
