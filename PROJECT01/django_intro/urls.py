"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/pong/', views.pong),
    path('home/ping/', views.ping),
    path('home/template_example/', views.template_example),
    path('home/isbirth/', views.isbirth),
    path('home/area/<int:R>/', views.area),
    path('home/mul/<int:num1>/<int:num2>/', views.mul),
    path('home/name_age/<name>/<int:age>/', views.name_age),
    path('home/cube/<int:num>/', views.cube),
    path('home/hello/<name>/', views.hello),
    path('home/index/', views.index),
    path('home/hola/', views.hola),
    path('home/dinner/', views.dinner),
    path('home/lotto/', views.lotto),
    path('admin/', admin.site.urls),
]
