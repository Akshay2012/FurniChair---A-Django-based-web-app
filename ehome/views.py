from django.shortcuts import render
from .models import Product
from .forms import CreateProduct
from cart.models import Order
# Create your views here.
def index(request):
    return render(request,'ehome/base.html')

def shop(request):
    product_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered = False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [order_item.product for order_item in user_order_items]

    context = { 
        'object_list': product_list, 
        'current_order_products': current_order_products
    }
    return render(request,'ehome/shop.html',context)

def create_product(request):
    form = CreateProduct(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "ehome/create_product.html",{'form':form})        