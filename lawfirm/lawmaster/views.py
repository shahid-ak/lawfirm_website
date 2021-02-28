from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'adminhome.html')
        return render(request,'home.html')
    return redirect('/login')

def login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST['uname']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/home')
        return render(request,'login.html')
    return redirect('/home')

def register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['password']         
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/register')
        user= User.objects.create_user(username=username, password=password, first_name=name,email=email)
        user.save()
        user = auth.authenticate(username=username,password=password)
        auth.login(request,user)
        return redirect('/home')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/home')