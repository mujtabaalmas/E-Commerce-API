from rest_framework import serializers
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Products
        fields = ['title','description','price','quantity','is_active','product_id',]



# class ProductsSerializer(serializers.Serializer):
#     title= serializers.CharField(max_length=255)
#     description = serializers.CharField()         
#     price = serializers.DecimalField(max_digits=6,decimal_places=2)
#     quantity = serializers.IntegerField()
#     is_active = serializers.BooleanField(read_only=True)
#     vender = serializers.PrimaryKeyRelatedField(read_only=True)
#     vendor_verified = serializers.BooleanField(source='vender.verified', read_only=True)
#     def create(self, validated_data):

#         #Creating and return a new `Products` instance, given the validated data.

#         return Products.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):

#        # Updating and returning an existing `Products` instance, given the validated data.
   
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.vender = validated_data.get('vender', instance.vender)
#         instance.vendor_verified = validated_data.get('vendor_verified', instance.vendor_verified)
#         instance.save()
#         return instance