from django.contrib import admin
from products.models import Products
# Register your models here.

#admin.site.register(Users)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','quantity','is_active','vender',)

admin.site.register(Products, ProductAdmin)

