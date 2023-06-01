from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm

def index(request):
    return render(request,'store/index.html')
def cart(request):
    context={}                                      
    return render(request,'store/cart.html',context)
def store(request):
    context={}                                      
    return render(request,'store/store.html',context)
def checkout(request):
    context={}                                      
    return render(request,'store/checkout.html',context)
def register(request):
    if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            uname=request.POST['username']
            password1=request.POST['password1']
            password2=request.POST['password2']
            
            myuser=User.objects.create_user(uname,email,password1)
            myuser.first_name=first_name
            myuser.last_name=last_name
            if password1 !=password2:
                messages.warning(request,'Password does not match')
                return render(request,'store/register.html')
            else:
                messages.success(request,'Account successfully created')
                myuser.save()

            
            
                                              
    return render(request,'store/register.html')
def login(request):                                   
    return render(request,'store/login.html')


