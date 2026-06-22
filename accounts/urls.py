from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('products/',products,name='products'),
    path('customer/<int:pk>/',customer,name='customer'),
    path('create_order/',createOrder,name='createorder'),
    path('update_order/<int:pk>/',updateOrder,name='updateorder'),
    path('delete_order/<int:pk>/',deleteOrder,name='deleteorder'),
    path('loginpage/',loginPage,name='loginpage'),
    path('registerpage/',registerPage,name='registerpage'),
    path('logout/',logoutPage,name='logout'),
    path('userpage/',userPage,name='userpage'),
    path('account/',customerSettings,name='customersettings'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]