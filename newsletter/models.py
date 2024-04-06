from django.db import models


class Newsletter(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
