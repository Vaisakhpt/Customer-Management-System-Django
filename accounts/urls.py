from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('products/',products,name='products'),
    path('customer/<int:pk>/',customer,name='customer'),
    path('create_order/',createOrder,name='createorder'),
    path('update_order/<int:pk>/',updateOrder,name='updateorder'),
    path('delete_order/<int:pk>/',deleteOrder,name='deleteorder'),
]