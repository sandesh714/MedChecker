from django.shortcuts import render, HttpResponse
from .models import Schedules
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    return render(request,'mainapp/index.html')

@login_required
def home(request):
    context = {
        'schedules' : Schedules.objects.all()
    }
    return render(request, 'mainapp/home.html',context)

