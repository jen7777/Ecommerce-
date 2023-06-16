from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name=models.CharField(max_length=255)
    prod_price=models.CharField(max_length=255)  
    prod_image=models.ImageField(upload_to='product')                #install pillow to upload pic
    def __str__(self):
        return self.prod_name