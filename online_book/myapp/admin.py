from django.contrib import admin
from .models import book

# Register your models here.
@admin.register(book)
class admin(admin.ModelAdmin):
    display_list = ['name', 'Price']
