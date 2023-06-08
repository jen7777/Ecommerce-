from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/',views.store,name='store'),
    path('register/',views.register,name='register'),
    path('login/',views.signin,name='signin'),
    
]