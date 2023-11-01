from django.contrib import admin
from django.urls import path
from user_auths import views

app_name = 'user_auths'

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('sign-out/', views.LogOutView, name='sign-out'),
    path('sign-in/', views.LoginView, name='sign-in'),
    path('sign-out/', views.LogOutView, name='sign-out'),
    
]