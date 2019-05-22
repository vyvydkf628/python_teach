from django.shortcuts import render, redirect
from .models import Board

def index(request):
    return render(request,'boards/index.html')

# Create your views here.