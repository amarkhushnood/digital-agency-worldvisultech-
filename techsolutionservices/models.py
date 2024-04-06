from django.db import models


class techservices(models.Model):
    techservices_icon = models.CharField(max_length=50)
    techservices_title = models.CharField(max_length=50)
    techservices_dec = models.TextField()

    def __str__(self):
        return self.techservices_title
