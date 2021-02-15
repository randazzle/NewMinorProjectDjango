from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import RegistrationForm, LoginForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #log the user in
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
