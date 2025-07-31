from rest_framework import serializers
from cart.models import Cart,CartItem
from products.models import Products

class CartItemSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title', read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'product_title',]

    # def create(self, validated_data):
    #     session_id = self.context.get('session_id')  # only use context
    #     if not session_id:
    #         raise serializers.ValidationError("Session ID is required.")

    #     cart, _ = Cart.objects.get_or_create(session_id=session_id)
    #     product = validated_data['product']                 
    #     quantity = validated_data['quantity']

    #     item, created = CartItem.objects.get_or_create(
    #         cart=cart, product=product,
    #         defaults={'quantity': quantity}
    #     )

    #     if not created:
    #         item.quantity += quantity
    #         item.save()

    #     return item

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        request = self.context.get('request')
        session_id = request.COOKIES.get('session_id')
        #session_id = self.context.get('session_id')
        if not session_id:
            raise serializers.ValidationError("Session ID is required  session id missing in cookies.")
        cart, _ = Cart.objects.get_or_create(session_id=session_id)
                                             # create a cart without giving any value, because session-id will be created in pre-save signal
        try:
            product = Products.objects.get(id=validated_data['product_id'], is_active=True)
        except Products.DoesNotExist:
            raise serializers.ValidationError("Product does not exist.")
        
        if validated_data['quantity'] > product.quantity:
            raise serializers.ValidationError(f"Only {product.quantity} of this product is available in stock.")
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            # Prevent cart quantity from exceeding available stock
            new_quantity = cart_item.quantity + validated_data['quantity']
            if new_quantity > product.quantity:
                raise serializers.ValidationError(f"Only {product.quantity} of this product is available in stock. Already Added {cart_item.quantity} products in your cart")
            
            cart_item.quantity = new_quantity
            # if cart_item.quantity > product.quantity:
            #     raise serializers.ValidationError(f"you have Already Added {cart_item.quantity} products in your cart")

        else:
            cart_item.quantity = validated_data['quantity']

        cart_item.save()
        return cart_item

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'product_id ': instance.product.id,
            'product_title': instance.product.title,
            'Total quantity': instance.quantity
        }
