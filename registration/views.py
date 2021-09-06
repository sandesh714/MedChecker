from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}")
            return redirect('main-home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form':form})

def login(request):
    
    return HttpResponse("<h1>Login</h1>")
    