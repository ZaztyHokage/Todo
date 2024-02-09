from django.shortcuts import render, redirect
from main.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')    


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        last_name = request.POST['last_name']
        user = User.objects.create_user(
            username=username, password=password, phone=phone, first_name=first_name, last_name=last_name
        )
        login(request, user)
        return redirect('index')
    return render(request, 'sign-up.html')
