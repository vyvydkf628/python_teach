from django.shortcuts import render, redirect
from .models import Board
def index(request):
    boards = Board.objects.all()[::-1]
    return render(request,'boards/index.html',{'boards':boards})

def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title,content=content)
    board.save()
    return redirect('boards:detail', board.pk)
    
def detail(request, pk):
    board= Board.objects.get(pk=pk)
    return render(request,'boards/detail.html',{'board':board})
    
def delete(request,pk):
    board= Board.objects.get(pk=pk)
    board.delete()
    return redirect('boards:index')
    
def edit(request,pk):
    board= Board.objects.get(pk=pk)
    return render(request,'boards/edit.html',{'board':board})
    
def update(request,pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('boards:detail',board.pk)