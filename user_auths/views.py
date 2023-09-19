from django.shortcuts import render, redirect
from user_auths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import time

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            new_user = form.save(commit=True) # creating a new variable so that we can access specific fields from form input
            username = form.cleaned_data.get('username')  # getting username from form input
            messages.success(request, f'Hey {username}, Your account has been created successfully!') # sending a success message
            time.sleep(2)  # wait for 2 seconds
            new_user = authenticate(username=form.cleaned_data['email'], # username_field in user model is email
                                    password=form.cleaned_data['password1'])
            print("Welcome, ", new_user)
            if new_user is not None:
                print("Successful sign-up - redirecting to home")
                login(request, new_user)
                return redirect('home')
        else: print("Form is not valid:", form.errors)
    
    elif request.user.is_authenticated:
        messages.warning(request, f'You are already logged in!')
        return redirect('home')
    
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)
    