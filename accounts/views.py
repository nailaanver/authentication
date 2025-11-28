    # myapp/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate, login

def welcome(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        myuser = User.objects.create_user(username,email,password)
        myuser.fname = first_name
        myuser.lname = last_name
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth_logout(request)