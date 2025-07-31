from django.db import models
from products.models import Products
import uuid
# # # Create your models here.

class Cart(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    #session_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # use signal to save session id. use pre-save signal

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

