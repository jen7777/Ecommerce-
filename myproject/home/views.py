from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
from .models import *                               # * means all functions

def index(request):
    return render(request,'store/index.html')
def home(request):
    return render(request,'store/home.html')
def cart(request):
    dict_prod={
        'cart':OrderItem.objects.all()                      #loading all products to store.html
    }     
                                 
    return render(request,'store/cart.html',dict_prod)
def store(request):
    dict_prod={
        'product':Product.objects.all()                      #loading all products to store.html
    }                                      
    return render(request,'store/store.html',dict_prod)
def checkout(request):
    context={}                                      
    return render(request,'store/checkout.html',context)
def register(request):
    if request.method=='POST':
            first_name=request.POST['first_name']              #getting each field seperately from reg.html
            last_name=request.POST['last_name']
            email=request.POST['email']
            uname=request.POST['username']
            password1=request.POST['password1']
            password2=request.POST['password2']
            
            myuser=User.objects.create_user(uname,email,password1)          #adding every fields to object myuser
            myuser.first_name=first_name
            myuser.last_name=last_name
            if password1 !=password2:
                messages.warning(request,'Password does not match')
                return render(request,'store/register.html')
            else:
                myuser.save()
                messages.success(request,'Account successfully created')
    return render(request,'store/register.html')               

def signin(request):
    if request.method=='POST':
            uname=request.POST['username']
            pass1=request.POST['password1']
            
            user=authenticate(username=uname,password=pass1)
            
            if user is not None:
                return render(request,'store/indexLogged.html')
            else:
                messages.warning(request,"Username or Password incorrect")
    return render(request,'store/login.html')     
                                            

