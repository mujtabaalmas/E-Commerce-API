from rest_framework import generics
from django.db.models import Count
from vendors.models import Vendors
from vendors.serializers import VendorsSerializer

class VendorListView(generics.ListAPIView):

    
    queryset = Vendors.objects.annotate(product_count=Count('vendor_products'))

    serializer_class = VendorsSerializer
