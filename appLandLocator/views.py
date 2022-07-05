from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

from .models import Land, Image
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


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('appLandLocator:index')
        else:
            message = {'message': 'Invalid Credentials'}
            return render(request, 'appLandLocator/login.html', message)
    return render(request, 'appLandLocator/login.html')


def logout_user(request):
    logout(request)
    return redirect('appLandLocator:index')


def index(request):
    infoCarousel = Land.objects.order_by("dateTime")
    infoImage = Image.objects.all()
    context = {
        'infoCarousel': infoCarousel,
        'infoImage': infoImage
    }
    return render(request, 'appLandLocator/index.html', context)
