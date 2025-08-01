from rest_framework import generics
from django.db.models import Count
from vendors.models import Vendors
from vendors.serializers import VendorsSerializer,VendorRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class VendorListView(generics.ListAPIView):

    queryset = Vendors.objects.annotate(product_count=Count('vendor_products'))

    serializer_class = VendorsSerializer
    permission_classes = [IsAuthenticated]

#class BecomeVendorView(APIView):
    # permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     user = request.user
    #     serializer = VendorRegistrationSerializer(data=request.data)

    #     if serializer.is_valid():
    #         store_name = serializer.validated_data['store_name']

    #         # Check if store_name already exists
    #         if Vendors.objects.filter(store_name=store_name).exists():
    #             return Response({'error': 'Store name already exists. Please choose another one.'}, status=400)

    #         # Check if user already registered as vendor
    #         if Vendors.objects.filter(user=request.user).exists():
    #             return Response({'error': 'You are already registered as a vendor.'}, status=400)

    #         Vendors.objects.create(
    #             user=request.user.email,
    #             store_name=store_name,
    #             verified=True,               # default, but you can explicitly set it
    #             joined_date=timezone.now()   # auto_now_add handles this too
    #         )

    #         return Response({'message': 'You have successfully registered as a vendor.'}, status=201)

    #     return Response(serializer.errors, status=400)

# class BecomeVendorView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user  #  This is a Users instance

#         # Check if user is already a vendor
#         if hasattr(user, 'vendor_profile'):  # OneToOneField has related_name='vendor_profile'
#             return Response({'error': 'You are already registered as a vendor.'}, status=400)

#         serializer = VendorRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             store_name = serializer.validated_data['store_name']

#             if Vendors.objects.filter(store_name=store_name).exists():
#                 return Response({'error': 'Store name already exists. Please choose another one.'}, status=400)

#             Vendors.objects.create(
#                 user=user,
#                 store_name=store_name,
#                 verified=True,
#                 joined_date=timezone.now()
#             )
#             return Response({'message': 'You have successfully registered as a vendor.'}, status=201)

#         return Response(serializer.errors, status=400)