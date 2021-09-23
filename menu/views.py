from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render


@login_required
def home(request): 
    return render(request,'registration/menu.html')


def ho(request):
    return render(request,'registration/base.html')
    
