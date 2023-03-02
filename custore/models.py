from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    size = models.CharField(max_length=50)
    def __str__(self):
        return self.size

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='files/', blank=True,null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.user.username
    


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name

class Orders(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.customer.name