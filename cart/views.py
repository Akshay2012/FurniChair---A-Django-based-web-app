from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from accounts.models import Profile
from ehome.models import Product
from .models import Order, OrderItem
from django.core.mail import send_mail   
# Create your views here.

def index(request):
    return render(request,'cart/home.html')

def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile,user=request.user)
    order = Order.objects.filter(owner=user_profile,is_ordered=False)
    if order.exists():
        return order[0]
    return 

@login_required()
def add_to_cart(request,pk):
    user_profile = get_object_or_404(Profile,user=request.user)
    try:
        product = Product.objects.get(id=pk)
        if product in user_profile.items.all():
            messages.info(request, 'This item has been purchased earlier!')
            return redirect(reverse('ehome:shop'))
        order_item = OrderItem.objects.filter(product=product)
        if len(order_item) == 0:
            order_item = OrderItem(product=product)
            order_item.save()
            order_item = [order_item]
        try:
            user_order  = Order.objects.get(owner=user_profile,is_ordered=False)
        except Order.DoesNotExist:
            user_order  = Order(owner=user_profile)
            user_order.save()
        for item in order_item:
            user_order.items.add(item)
            user_profile.items.add(item.product)
        user_order.save()
        user_profile.save()
        messages.info(request,"This product has been added to the cart!")
    except Product.DoesNotExist:
        messages.info(request,"Product Not Found")
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

@login_required()
def sendmail(request):
    subject = 'Greetings from Furnichair!'
    msg = """
        Thank you for purchasing from FurniChair!
    """
    send_mail(
        'Greetings from FurniChair!',
        'Thank you for purchasing from FurniChair!',
        'shah.ayush100@gmail.com',
        ['akshayagrawal705@gmail.com',settings.EMAIL_HOST_USER],
        fail_silently=False
    )
    return render(request,'cart/thank.html')