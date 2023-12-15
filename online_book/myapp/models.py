from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Create your models here.
class book(models.Model):
    Name = models.CharField(max_length=200)
    Author = models.CharField(max_length=200, null=True)
    Publisher = models.CharField(max_length=200, null=True)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='Images', null=True, blank=True)
    category = models.CharField(max_length=100, default=False)
    Language = models.CharField(max_length=100, default=False)
    Genra = models.CharField(max_length = 100, default = False)
    time = models.DateField(auto_now_add=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    website = models.ForeignKey(book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True)

class Address(models.Model):
    City = models.CharField(max_length=50, null=True)
    Pincode = models.IntegerField(null=True)
    State = models.CharField(max_length=50, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Buy_direct = models.ForeignKey(book, on_delete=models.CASCADE, null=True)
    Buy_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order_id = models.IntegerField(null=True, unique=True)
    