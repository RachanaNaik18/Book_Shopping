from django.contrib import admin
from .models import book,Cart,Order,Address

# Register your models here.
@admin.register(book)
class admin1(admin.ModelAdmin):
    display_list = ['name', 'Price']

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Address)