from django.db import models


class contactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
