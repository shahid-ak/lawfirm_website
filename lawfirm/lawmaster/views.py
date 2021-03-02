from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Field, Lawyers
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    if request.user.is_authenticated:
        fields = Field.objects.all()
        lawyers = Lawyers.objects.all()
        if request.user.is_superuser:
            return render(request,'adminhome.html',{'fields':fields, 'lawyers':lawyers})
        return render(request,'home.html',{'fields':fields, 'lawyers':lawyers})
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

def addnew(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                name = request.POST['name']
                lawSchool = request.POST['lawSchool']
                recognisedSince = request.POST['recognisedSince']
                phone = request.POST['phone']
                languages = request.POST['languages']
                location = request.POST['location']
                bio = request.POST['bio']
                field = request.POST['field']
                img = request.FILES['img']
                submit = Lawyers(img = img, name = name, lawSchool = lawSchool, recognisedSince = recognisedSince, phone = phone, languages = languages, location = location, bio = bio, field = field)
                submit.save()
                return redirect('/home')
            fields = Field.objects.all() 
            return render(request,'addnew.html',{'fields':fields})
    return redirect('/login')

def addfield(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                name = request.POST['name']
                submit = Field(fieldName=name)
                submit.save()
            fields = Field.objects.all() 
            return render(request,'addnew.html',{'fields':fields})
    return redirect('/login')

def viewLawyer(request, id):
    if request.user.is_authenticated:
        lawyer = Lawyers.objects.get(id=id)
        if request.user.is_superuser:
            return render(request,'adminViewLawyer.html',{'lawyer':lawyer})
        return render(request,'viewLawyer.html',{'lawyer':lawyer})
    return redirect('/login')

def deleteLawyer(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            lawyer = Lawyers.objects.get(id=id).delete()
            return redirect('/home')
    return redirect('/login')

def allusers(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.all()
            return render(request,'allusers.html',{'users':users})
    return redirect('/login')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/home')