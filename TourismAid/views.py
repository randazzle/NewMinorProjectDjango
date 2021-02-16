from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):	# *args, **kwargs
	return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact_us.html')

def sign_up(request):
    return render(request, 'sign_up.html')
