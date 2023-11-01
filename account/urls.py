from django.contrib import admin
from django.urls import path
from user_auths import views
from account import views

urlpatterns = [
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
]
