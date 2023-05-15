from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
# Create your models here.
