from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/',views.store,name='store'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]