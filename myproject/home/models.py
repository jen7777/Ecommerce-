from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    prod_name=models.CharField(max_length=255)
    prod_price=models.CharField(max_length=255)  
    prod_image=models.ImageField(upload_to='product')                #install pillow to upload pic
    def __str__(self):
        return self.prod_name
    
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)  #one user has only one customer
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True) #one to many bcoz one customer can have many orders
    date_ordered=models.DateTimeField(auto_now_add=True)
    transaction_id=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return str(self.transaction_id)      #as id is integer, need to be converted into string
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    zipcode=models.CharField(max_length=50,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.address
