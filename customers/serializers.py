from rest_framework import serializers
from customers.models import Customer

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['session_id', 'name', 'email']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email','session_id', 'id', 'created_at',]
        extra_kwards = {
            'session_id': {'required': False},
            'name': {'required': False},
            'email': {'required': False},            
        }   