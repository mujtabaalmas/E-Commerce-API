from django.db import models
from users.models import Users

class Vendors(models.Model):
    # user  = models.CharField() # (FK to User) in apply user model
    store_name= models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='vendor_profile', null=True)
    
    def __str__(self):
        return self.store_name

"""
from vendors.models import Vendors
from vendors.serializers import VendorsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

ok  = Vendors(user="okgoogle1") 
serializer = VendorsSerializer(Vendors)

"""