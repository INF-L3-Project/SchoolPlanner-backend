from django.db import models
from django.contrib.auth.models import User


class Institution(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    logo = models.ImageField(blank=True, null=True, upload_to="logo/")
    description = models.TextField()

    
    def __str__(self):
        return self.name
