from django.contrib import admin
from cart.models import Cart,CartItem
# # Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('session_id','created_at',)

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity',)

admin.site.register(CartItem, CartItemAdmin)