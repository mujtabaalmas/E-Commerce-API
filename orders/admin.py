from django.contrib import admin
from orders.models import Order,OrderItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('session_id','customer','created_at',)

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity',)

admin.site.register(OrderItem, OrderItemAdmin)



