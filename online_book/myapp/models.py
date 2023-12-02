from django.db import models

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

