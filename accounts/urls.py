from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.my_profile,name='my_profile')
]
