from django.shortcuts import render
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
    context={}                                      
    return render(request,'store/register.html',context)
def login(request):                                   
    return render(request,'store/login.html')


