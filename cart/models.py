from django.db import models
from accounts.models import Profile
from ehome.models import Product

# Create your models here.

# class OrderManager(models.Manager):
#     def get_or_create(self,*args, **kwargs):


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL,null = True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now = True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now = True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.cost for item in self.items.all()])

        

