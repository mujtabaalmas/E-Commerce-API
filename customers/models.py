import uuid
from django.db import models
from django.utils import timezone

# class Customers(models.Model):
#     session_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
    
#     def __str__(self):
#         return self.email

class Customer(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(null=True)
    
    # def __str__(self):
    #     return self.email
    
    