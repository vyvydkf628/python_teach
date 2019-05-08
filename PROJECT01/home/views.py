import random

from datetime import datetime
from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')

#self-introduction    
def hola(request):
    return render(request, 'hola.html')


def dinner(request):
    menus = ['pizza','bab','chicken','sushi']
    picked = random.choice(menus)
    context = {'menus':menus,'picked':picked}
    return render(request,'dinner.html',context)
    
def lotto(request):
    numbers = range(1,46)
    tks = 0
    lottos = random.sample(numbers,6)
    real_lottos = [6,10,17,29,39,41]
    context = {'lottos':lottos,'real_lottos':real_lottos,'tks':tks}
    return render(request,'lotto.html',context)
    
def hello(request, name):
    return render(request,'hello.html',{'name':name})

def cube(request,num):
    nums = num **3
    return render(request,'cube.html',{'num':num,'nums':nums})

def name_age(request, name, age):
    return render(request,'name_age.html',{'name':name,'age':age})

def mul(request,num1,num2):
    time = num1 *num2
    return render(request,'mul.html',{'num1':num1,'num2':num2,'time':time})
    
def area(request, R):
    half = R*R*3.14
    return render(request,'area.html',{'R':R,'half':half})
    
    
# isbirth

def isbirth(request):
    today = datetime.now()
    result = False
    if today.month == 6 and today.day ==28:
        result = True
    else :
        result = False
    return render(request,'isbirth.html',{'result': result})
    
def template_example(request):
    my_list = ['짜장면','탕수육','짬뽕','양장피']
    messages = ['apples','bananas','mango']
    empty_list = []
    return render
    
    
def ping(request):
    return render(request,'ping.html')

def pong(request):
    data = request.GET.get('data')
    return render(request, 'pong.html',{'data':data})









