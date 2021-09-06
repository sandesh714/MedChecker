from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}")
            return redirect('main-home')
    else:
        form = UserRegistration()

    return render(request, 'registration/signup.html', {'form':form})

def login(request):
    
    return HttpResponse("<h1>Login</h1>")
    