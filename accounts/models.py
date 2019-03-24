from django.db import models
from django.conf import settings
from ehome.models import Product

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username