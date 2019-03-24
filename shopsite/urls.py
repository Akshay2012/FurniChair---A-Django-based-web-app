from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('ehome.urls',namespace='products')),
    path('admin/', admin.site.urls),
    path('shop/',include('ehome.urls',namespace='products')),
    path('profiles/',include('accounts.urls',namespace='accounts')),
    path('cart/',include('cart.urls',namespace='cart')),
]
