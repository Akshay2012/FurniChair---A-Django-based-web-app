from django.urls import path,include
from . import views

app_name = 'ehome'

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
]
