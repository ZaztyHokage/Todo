from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone


def index_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('index')
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)


def complete_view(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = 1
    todo.updated_at = timezone.now()
    todo.save()
    return redirect('index')


def delete_view(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = 2
    todo.updated_at = timezone.now()
    todo.save()
    return redirect('index')


def in_progress_view(request):
    progres = Todo.objects.filter(status=0).order_by('-id')
    return render(request, 'inprog.html', {'progres': progres})


def deleted_view(request):
    if request.method == 'POST':
        text = request.POST['search']
        progres = Todo.objects.filter(status=2, title__icontains=text).order_by('-id')
        return render(request, 'deleted.html', {'progres': progres})
    progres = Todo.objects.filter(status=2).order_by('-id')
    return render(request, 'deleted.html', {'progres': progres})


def completed_view(request):
    progres = Todo.objects.filter(status=1).order_by('-id')
    return render(request, 'finished.html', {'progres': progres})






