from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    phone=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    profilepic=models.ImageField(default='profile.png',null=True,blank=True)

    def __str__(self):
        return self.name   

class Tag(models.Model):
    tag_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.tag_name    

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=200,choices=(('indoor','indoor'),('outdoor','outdoor')))
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,choices=(('cancelled','cancelled'),('pending','pending'),('Delivered','Delivered')))
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.customer:
            return f"{self.customer.name} - {self.product.product_name}"
        return f"Deleted Customer- {self.product.product_name}"




    