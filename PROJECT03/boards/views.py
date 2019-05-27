from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm
def index(request): 
    boards = Board.objects.all()[::-1]
    return render(request,'boards/index.html',{'boards':boards} )

@login_required
def create(request):
    if request.method =='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.pk)
        
    else :
        form = BoardForm()
        return render(request,'boards/form.html',{'form': form})

# def edit(request,board_pk):
#     board = get_object_or_404(Board,pk=board_pk)
#     if request.method == 'POST':
#         form = BoardForm(request.POST, instance = board)
#         if form.is_valid():
#             board = form.save()
#         return redirect('boards:detail',board.pk)
#     else :
#         form = BoardForm(instance = board)
#         return render(request, 'boards/form.html',{'form':form, 'board':board})

def detail(request,board_pk):
    board = get_object_or_404(Board, pk = board_pk)
    
    return render(request,'boards/detail.html',{'board': board})

def delete(request,board_pk):
    board = get_object_or_404(Board, pk = board_pk)
    
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else :
        return redirect('boards:detail',board_pk)
# Create your views here.