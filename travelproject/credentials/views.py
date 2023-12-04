import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        from django.contrib import auth
        user=auth.authenticate(username=username,password=password)
        from django.contrib import messages
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login/')

    return render(request,'login.html')
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword =request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                from django.contrib import messages
                messages.info(request,"username taken")
            elif User.objects.filter(email=email).exists():
                from django.contrib import messages
                messages.info(request, "email taken")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save()
                 print("user created")
        else:
            from django.contrib import messages
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
