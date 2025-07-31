from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)

    def create(self, validated_data):

        #Creating and return a new `Vendor` instance, given the validated data.

        return Users.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

       # Updating and returning an existing `Vendor` instance, given the validated data.
   
        # instance.user = validated_data.get('user', instance.user)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance