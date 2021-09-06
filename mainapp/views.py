from django.shortcuts import render, HttpResponse
from .models import Schedules
# Create your views here.

def index(request):
    
    return render(request,'mainapp/index.html')

def home(request):
    context = {
        'schedules' : Schedules.objects.all()
    }
    return render(request, 'mainapp/home.html',context)

