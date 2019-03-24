from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from accounts.models import Profile
from ehome.models import Product
from .models import Order, OrderItem
   
# Create your views here.
def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile,user=request.user)
    order = Order.objects.filter(owner=user_profile,is_ordered=False)
    if order.exists():
        return order[0]
    return 

@login_required()
def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile,user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    if product in request.user.profile.items.all():
        messages.info(request, 'This item has been purchased earlier!')
        return redirect(reverse('ehome:shop'))
    order_item , status = OrderItem.objects.get_or_create(product=product)
    user_order , status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
    messages.info(request,"This product has been added to the cart!")
    return redirect(reverse('ehome:shop'))

@login_required()
def delete_from_cart(request,pk):
    product_to_delete = OrderItem.objects.filter(pk=pk)
    if product_to_delete.exists():
        product_to_delete[0].delete()
        messages.info(request,"The product has been removed from the cart!")
    return redirect(reverse('cart:summary'))

@login_required()
def order_details(request,**kwargs):
    current_order = get_user_pending_order(request) 
    return render(request, 'cart/summary.html',{'order':current_order})   