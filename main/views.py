from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.views import login_view

@login_required(login_url='login')
def index_view(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(user=user, title=title)
        return redirect('index')
    context = {
        'todos': Todo.objects.filter(user=user)
    }
    return render(request, 'index.html', context)


def complete_view(request, pk):
    user = request.user
    todo = Todo.objects.get(user=user, pk=pk)
    todo.status = 1
    todo.updated_at = timezone.now()
    todo.save()
    return redirect('index')


def delete_view(request, pk):
    user = request.user
    todo = Todo.objects.get(user=user, pk=pk)
    todo.status = 2
    todo.updated_at = timezone.now()
    todo.save()
    return redirect('index')

@login_required(login_url='login')
def in_progress_view(request):
    user = request.user
    progres = Todo.objects.filter(user=user, status=0).order_by('-id')
    return render(request, 'inprog.html', {'progres': progres})

@login_required(login_url='login')
def deleted_view(request):
    user = request.user
    if request.method == 'POST':
        text = request.POST['search']
        progres = Todo.objects.filter(user=user, status=2, title__icontains=text).order_by('-id')
        return render(request, 'deleted.html', {'progres': progres})
    progres = Todo.objects.filter(status=2).order_by('-id')
    return render(request, 'deleted.html', {'progres': progres})

@login_required(login_url='login')
def completed_view(request):
    user = request.user
    progres = Todo.objects.filter(user=user, status=1).order_by('-id')
    return render(request, 'finished.html', {'progres': progres})






