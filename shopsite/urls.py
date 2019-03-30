from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('ehome.urls',namespace='products')),
    path('profiles/',include('accounts.urls',namespace='accounts')),
    path('cart/',include('cart.urls',namespace='cart')),
]
