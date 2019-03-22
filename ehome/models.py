from django.db import models

# Create your models here.
class Product(models.Model):
    imgurl = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()

    def __str__(self):
        return self.name