from rest_framework import serializers
from vendors.models import Vendors

class VendorsSerializer(serializers.Serializer):
    # user  = serializers.CharField()# (FK to User)
    store_name= serializers.CharField(max_length=255)
    verified = serializers.BooleanField(read_only=True)
    joined_date = serializers.DateTimeField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product_count = serializers.IntegerField()

   # products = serializers.PrimaryKeyRelatedField(read_only=True)
    #user = serializers.OneToOneField(serializers, on_delete=serializers.CASCADE, related_name='vendor_profile')

    def create(self, validated_data):

        #Creating and return a new `Vendor` instance, given the validated data.

        return Vendors.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

       # Updating and returning an existing `Vendor` instance, given the validated data.
   
        # instance.user = validated_data.get('user', instance.user)
        instance.store_name = validated_data.get('store_name', instance.store_name)
        instance.verified = validated_data.get('verified', instance.verified)
        instance.joined_date = validated_data.get('joined_date', instance.joined_date)
        instance.user = validated_data.get('user', instance.user)

        instance.save()
        return instance