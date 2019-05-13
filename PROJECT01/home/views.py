import random, requests

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
    
def catch(request):
    return render(request, 'catch.html')
    
# artii API 를 통해 ascii 아트로 변환하여 보여주는 페이지
def result(request):
    #1. form 태그로 날린 데이터를 받는다. (GET 방식)
    word= request.GET.get('word')
    
    #2. ARTII api 로 보낸 응답 결과를 텍스트로 폰트라는 변수에 저장
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    #3. fonts(str)를 fonts(list)로 바꿔준다.
    fonts = fonts.split('\n')
    #4. fonts(list)안에 들어있는 요소중 하나를 선택해서  font라는 변수에 저장한다.
    font = random.choice(fonts)
    #5 위에서 우리가 만든 word와 font를 가지고 다시 artii로 요청을 보낸 후에 해당 응답 결과를 result라는 변수에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    return render(request,'result.html',{'result':result})
    

def throw(request):
    return render(request,'throw.html')

def get(request):
    data = request.GET.get('data')
    
    numbers = range(1,46)
    lottos = random.sample(numbers,6)
    real_lottos = [6,10,17,29,39,41]
    return render(request,'get.html',{'data':data,'lottos':lottos,'real_lottos':real_lottos})




def user_new(request):
    return render(request,'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    return render(request,'user_create.html',{'name':name,'pwd':pwd})