from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('item/delete/<int:pk>/',views.delete_from_cart,name='delete_item'),
    path('summary/',views.order_details,name='summary')
]
