from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('confrim password')
        user=User.objects.create_user(username=username,password=password)
        user.save();
        return redirect('/login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password=request.POST['password']
        userauth=auth.authenticate(username=username1,password=password)

        if userauth is not None:
            auth.login(request,userauth)
            return redirect('/new')
        else:
            messages.info(request,"invalid")
            return  redirect('/login')
    return render(request,"login.html")

def new(request):
    return render(request,"new.html")

def form(request):
    if request.method=='POST':
        return redirect('/appl')

    return render(request,"form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def appl(request):
    return render(request,"appl.html")