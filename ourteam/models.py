from django.db import models


class Ourteam(models.Model):
    per_icon = models.CharField(max_length=50)
    per_name = models.CharField(max_length=50)
    # per_designation = models.CharField(max_length=50)

    def __str__(self):
        return self.per_name


# Create your models here.
