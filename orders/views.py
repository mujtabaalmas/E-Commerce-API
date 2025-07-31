
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckoutSerializer

class CheckoutView(APIView):
    def post(self, request):
        # session_id = request.COOKIES.get('session_id')
        serializer = CheckoutSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({'message': 'Order placed successfully'}, status=201)
        return Response(serializer.errors, status=400)
