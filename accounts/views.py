    # myapp/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate, login

def welcome(request):
    return render(request,'accounts/welcome.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            first_name= user.first_name
            return render(request,'accounts/index.html',{'first_name':first_name})
        else:
            messages.error(request,"invalid credentials")
            return redirect(welcome)
    return render(request,'accounts/login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        myuser = User.objects.create_user(username,email,password,confirm_password)
        myuser.fname = first_name
        myuser.lname = last_name
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('login')
    return render(request,'accounts/register.html')
def logout_view(request):
    auth_logout(request)
    return redirect('login')