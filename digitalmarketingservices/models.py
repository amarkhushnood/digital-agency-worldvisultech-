from django.db import models


class digitalservices(models.Model):
    digitalservices_icon = models.CharField(max_length=50)
    digitalservices_title = models.CharField(max_length=50)
    digitalservices_dec = models.TextField()

    def __str__(self):
        return self.digitalservices_title
