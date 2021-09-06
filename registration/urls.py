
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.signup),
    path('login/',views.login)

   
]
