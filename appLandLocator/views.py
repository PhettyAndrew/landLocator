from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect, get_object_or_404

from .models import Land, Image
from .forms import UserForm, LandForm, ImageForm


# Create your views here.


# Signup Function
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


# Login Function
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


# Logout Function
def logout_user(request):
    logout(request)
    return redirect('appLandLocator:index')


# Home Page Function
def index(request):
    infoLand = Land.objects.order_by('?')
    context = {
        'infoLand': infoLand,
    }
    return render(request, 'appLandLocator/index.html', context)


# Lands Page Function
def lands(request):
    infoLand = Land.objects.all()
    context = {
        'infoLand': infoLand,
    }
    return render(request, 'appLandLocator/lands.html', context)


# Land Details Page Function
def landDetails(request, landId):
    infoLandDetails = get_object_or_404(Land, landCode=landId)
    infoImage = Image.objects.filter(land__landCode__contains=landId)
    context = {
        'infoLandDetails':infoLandDetails,
        'infoImage':infoImage,
    }
    return render(request, 'appLandLocator/land-details.html', context)


# Upload Land Function
def uploadLand(request):
    landForm = LandForm(request.POST or None, request.FILES or None)
    if landForm.is_valid():
        landForm.save()
        return redirect('appLandLocator:lands')
    context = {
        'landForm': landForm,
    }
    return render(request, 'appLandLocator/upload-land.html', context)


# Delete Land Function
def deleteLand(request, land_code):
    land = get_object_or_404(Land, landCode=land_code)
    land.delete()
    return redirect('appLandLocator:lands')


# Update Land Function
def updateLand(request, land_code):
    land = get_object_or_404(Land, landCode=land_code)
    landForm = LandForm(request.POST or None, request.FILES or None, instance=land)

    if landForm.is_valid():
        landForm.save()
        return redirect('appLandLocator:lands')
    return render(request, 'appLandLocator/upload-land.html', {'landForm': landForm})
