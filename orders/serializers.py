
from rest_framework import serializers
from .models import  Customer, Order, OrderItem
from cart.models import Cart

class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()    

    def validate(self, data):
        name = data.get('name')
        email = data.get('email')
        if Customer.objects.filter(name=name, email=email).exists():
            raise serializers.ValidationError("An order has already been placed with this name and email.")
        return data
    
    def create(self, validated_data):

        request = self.context.get('request')
        session_id = request.COOKIES.get('session_id')

        if not session_id:
            raise serializers.ValidationError("Session ID is required  session id missing in cookies.")
                
        try:
            cart = Cart.objects.get(session_id=session_id)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("No cart found for this session.")
        

        customer, created = Customer.objects.get_or_create(
        session_id=session_id,
        defaults={
            'name': validated_data['name'],
            'email': validated_data['email']
        }
        )

        # If customer exists, update name/email
        if not created:
            customer.name = validated_data['name']
            customer.email = validated_data['email']
        customer.save()
        # # Create or get customer
        # customer, _ = Customer.objects.get_or_create(
        #     session_id=session_id,
        #     defaults={
        #         'name': validated_data['name'],
        #         'email': validated_data['email']
        #     }
        # )
        # if not _:
        # customer.name = validated_data['name']
        # customer.email = validated_data['email']
        # customer.save()
        # # Create the order with foreign key to customer
        order = Order.objects.create(
            customer=customer,
            session_id=session_id
        )

        # Add items from cart
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Clear the cart

        cart.delete()

        return order
