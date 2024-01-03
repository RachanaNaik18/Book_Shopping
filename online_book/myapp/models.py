from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
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
    website = models.ForeignKey(book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Address(models.Model):
    street= models.CharField(max_length=250, null=True)
    City = models.CharField(max_length=50, null=True)
    Pincode = models.IntegerField(null=True)
    State = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(book, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Buy_direct = models.ForeignKey(book, on_delete=models.CASCADE, null=True)
    Buy_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length = 100, null=True, unique=True)
    date = models.DateField(auto_now_add=True, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            current_time = datetime.now()
            order_id = f"{current_time.strftime('%Y%d%M%H%M%S')}-{uuid.uuid4().hex[:5]}"
            self.order_id = order_id
        super().save(*args, **kwargs)

class Delivered(models.Model):
    book_Cart = models.ForeignKey(book, on_delete= models.CASCADE, null=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_id_no = models.CharField(max_length = 100, null=True, unique=True)
    date_ord = models.DateField(auto_now_add=True, null=True)
    date = models.DateField(null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    Cur_add = models.CharField(max_length=900, null=True)


