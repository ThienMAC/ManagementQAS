from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    
    if request.method=='GET':
        return render(request,'users/login.html')


    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user:
            auth_login(request,user)
            return redirect('home')

    msg=f'Invalid username or password'
    print(msg)
    context={
        'msg':msg
    }
    return render(request,'users/login.html',context)


