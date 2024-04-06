from django.contrib import admin
from ourteam.models import Ourteam


class OurteamAdmin(admin.ModelAdmin):
    List_display = ("per_icon", "per_name", "per_designation")


admin.site.register(Ourteam, OurteamAdmin)
# Register your models here.
