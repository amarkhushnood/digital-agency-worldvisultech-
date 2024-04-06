from django.db import models


class graphicservices(models.Model):
    graphicservices_icon = models.CharField(max_length=50)
    graphicservices_title = models.CharField(max_length=50)
    graphicservices_dec = models.TextField()

    def __str__(self):
        return self.graphicservices_title
