from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Cart,CartItem
from cart.serializers import AddToCartSerializer,CartItemSerializer
from uuid import uuid4


class AddToCartView(APIView):
    def post(self, request):
        # session_id = request.headers.get('Session-id')  # UUID from frontend
        # if not session_id:
        #     return Response({"error": "Session-Id header missing"}, status=400)

        serializer = AddToCartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            cart_item = serializer.save()
            #print("session id used for add to cart: ",request.session_id)
            #print(request)
            return Response({
                "message": "Product added to cart.",
                "item": serializer.data
            }, status=201)
        #print("session id used for add to cart: ",session_id)
        return Response(serializer.errors, status=400)
    
    # use nested serializer to view cart with cartItem


    
# class CartView(APIView):
#     def get(self, request):
#         session_id = request.COOKIES.get('session_id')
#         #session_id = request.headers.get('Session-id')
#         if not session_id:
#             return Response({"error": "Session-id in cookies missing"}, status=400)
#         try:
#             cart = Cart.objects.get(session_id=session_id)
#             serializer = CartItemSerializer(cart.items.all(), many=True)
#             return Response(serializer.data)
#         except Cart.DoesNotExist:
#             return Response([], status=200)

class CartView(APIView):
    def get(self, request):
        session_id = request.COOKIES.get('session_id')
        if not session_id:
            return Response({"error": "Session-id in cookies missing"}, status=400)
        try:
            cart = Cart.objects.get(session_id=session_id)
        except Cart.DoesNotExist:
            return Response({"message": "Your Cart is Empty", "total_cart_price": 0.0}, status=200)

        items = cart.items.all()
        
        serializer = CartItemSerializer(cart.items.all(), many=True)

        total_price = sum(item.quantity * item.product.price for item in items)

        return Response({
            "items": serializer.data,
            "total_cart_price": round(total_price, 2)
        })
