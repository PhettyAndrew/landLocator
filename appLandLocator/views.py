from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        reg = form.save(commit=False)
        reg.set_password(password)
        reg.save()
        logout(request)
        return redirect('appLandLocator:index')
    return render(request, 'appLandLocator/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request)
            return redirect('appRadical:index')
        else:
            message = {'message': 'Invalid Credentials'}
            return render(request, 'appLandLocator/login.html', message)
    return render(request, 'appLandLocator/login.html')


def index(request):
    return render(request, 'appLandLocator/index.html')