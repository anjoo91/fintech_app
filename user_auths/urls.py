from django.contrib import admin
from django.urls import path
from user_auths import views

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('sign-out/', views.LogOutView, name='sign-out'),
    
]