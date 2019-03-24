from django.shortcuts import render,get_object_or_404
from cart.models import Order
from .models import Profile

# Create your views here.
def my_profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    user_orders = Order.objects.filter(is_ordered=True, owner=user_profile)
    return render(request,'profile.html',{ 'user_orders':user_orders })