from django.shortcuts import render,redirect
from .models import Room, UserProfile
from .models import Account, MultipleImage
from .forms import uploadForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.utils import IntegrityError

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')
    context = {'page':page}
    return render(request, 'base/login_register.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')
    return render(request, 'base/login_register.html', {'form': form})

from django.contrib import messages
from django.db import IntegrityError

@login_required(login_url='login')
def home(request):
    uProfile = UserProfile.objects.get(user=request.user)
    images = MultipleImage.objects.all()
    form = uploadForm()
    if request.method == 'POST':
        form = uploadForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.profile = uProfile
            try:
                account.save()
                messages.success(request, 'Account created successfully!')
            except IntegrityError:
                messages.error(request, 'An account with that username already exists for this user.')
            return redirect('home')
    context = {'uProfile':uProfile, 'images':images, 'form':form}
    return render(request, 'base/home.html', context)




def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'rooms':rooms}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def updateForm(request, pk):
    uAccount = Account.objects.get(id=pk)
    form = uploadForm(instance=uAccount)
    if request.method == 'POST':
        form = uploadForm(request.POST, instance=uAccount)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        account_id = request.POST.get('account_id')
        account = Account.objects.get(id=account_id)
        for image in images:
            MultipleImage.objects.create(account=account, images=image)
        return redirect('home')
    else:
        rooms = Room.objects.all()
        images = MultipleImage.objects.all()
        context = {'rooms':rooms, 'images': images}
        return render(request, 'base/home.html', context)

@login_required(login_url='login')
def deleteForm(request, pk):
    uAccount = Account.objects.get(id=pk)
    if request.method == 'POST':
        uAccount.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {})