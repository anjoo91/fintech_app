from django.shortcuts import render, redirect
from user_auths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save() # creating a new variable so that we can specific fields from form input
            username = form.cleaned_data.get('username')  # getting username from form input
            messages.success(request, f'Hey {username}, Your account has been created successfully!') # sending a success message
            new_user = authenticate(username=form.cleaned_data['username'], 
                                    password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)
    