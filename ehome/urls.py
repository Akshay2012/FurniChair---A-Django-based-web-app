from django.urls import path,include
from . import views

app_name = 'ehome'

urlpatterns = [
    path('',views.shop,name='shop'),
]
