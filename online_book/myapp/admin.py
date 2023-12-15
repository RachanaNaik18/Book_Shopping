from django.contrib import admin
from .models import book,Cart

# Register your models here.
@admin.register(book)
class admin1(admin.ModelAdmin):
    display_list = ['name', 'Price']

# @admin.register(Cart)
# class admin1(admin.ModelAdmin):
#     display_list = '__all__'
admin.site.register(Cart)