from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return render(request,'ehome/base.html')

def shop(request):
    product_list = Product.objects.all()
    context = { 'object_list': product_list }
    return render(request,'ehome/shop.html',context)