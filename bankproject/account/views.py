from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('confrim password')
        user=User.objects.create_user(username=username,password=password)
        user.save();
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        userauth=auth.authenticate(username=username,password=password)

        if userauth is not None:
            auth.login(request,userauth)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return  redirect('/login/')
    return render(request,"login.html")