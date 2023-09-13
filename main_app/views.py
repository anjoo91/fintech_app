# Django Packages
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Models

# Forms


# Create your views here.

# Home View ("/")
def home(request):
    return render(request, 'home.html')

# About View ("/about")
def about(request):
    return render(request, 'about.html')
    
    