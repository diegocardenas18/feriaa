from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    #appcore
    
    path('inicio', views.home , name='home'),
    path('', views.ho , name='ho'),

    
]