from django.db import models
from vendors.models import Vendors

class Products(models.Model):
    vender  = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendor_products', null=False, default=False) #  Products should not exist without a Vendor foreign key be null if not vender product
    title= models.CharField(max_length=255)
    description = models.CharField()         
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=False)
    