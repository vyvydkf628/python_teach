from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Welcome to Django!")

#self-introduction    
def hola(request):
    return HttpResponse("my name is DongCheol")
    
# food


# Create your views here.
