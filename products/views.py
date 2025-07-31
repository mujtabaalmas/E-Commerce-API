# from rest_framework.decorators import  APIView, api_view
# from rest_framework.response import Response
# from rest_framework import generics
# from .models import Products
# from products.serializers import ProductsSerializer
# from customers.models import Customer
# from django.dispatch import receiver
# from django.db.models.signals import (pre_save, post_save)
# import uuid

# product
#order
# itemcart
# User Permission (do this)
# Upload whole project to Github (you should know git fetch, git pull, git status, git commit, git push, git stash, git restore, git merge, git add)
# you should also know the difference between stag files, origin, remote, branch, stash


# products/views.py
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from products.serializers import ProductsSerializer
from customers.models import Customer
import uuid

@api_view(['GET'])
def get_products_by_requests(request):
    # Get session_id from cookie
    session_id = request.COOKIES.get('session_id')
    created_new = False

    if not session_id:
        # Generate new session_id and create customer
        session_id = str(uuid.uuid4())
        Customer.objects.create(session_id=session_id)
        created_new = True
    else:
        # Check if customer exists; if not, create one
        Customer.objects.get_or_create(session_id=session_id)

    # Fetch products
    products = Products.objects.filter(is_active=True, vender__verified=True)
    serializer = ProductsSerializer(products, many=True)

    # Prepare response
    response = Response({
        'session_id': session_id,
        'products': serializer.data
    })

    if created_new:
        # Set session_id in cookie if it was newly created
        expiry = datetime.utcnow() + timedelta(seconds=300)
        response.set_cookie('session_id', session_id,expires=expiry)
        
        #response.set_cookie('session_id', session_id, max_age=10)  #60*60*24*30
        print("this time left in expiry ", str(expiry))
    print("session id: ",session_id) 
    return response

# @api_view(['GET'])
# def get_products_by_requests(request):
#     if request.method == 'GET':
#         products = Products.objects.filter(is_active=True, vender__verified=True)
#         serializer = ProductsSerializer(products, many=True)
#         return Response({
#             'products':serializer.data
#         })
            
    
# class get_products_by_requests(APIView):
#     def products_list(self, request):
#         #session_id = request.session_id
#         queryset = Products.objects.filter(is_active=True, vender__verified=True)[:10]
#         serializer_products = ProductsSerializer(queryset, many=True)
#         # # return Response(serializer_products.data)
#         return Response({
#             #'session_id': session_id,
#             'queryset': serializer_products.data
#         })
        # return Response(serializer_products)

# class ProductListView(generics.ListAPIView):   

#     queryset = Products.objects.filter(is_active=True, vender__verified=True)
#     # def get_products_request(request):
#     # def get_queryset(self):
#     #    # return super().get_queryset() 
#     #     return Products.objects.filter(is_active=True, vender__verified=True)

#     #print("Total Active Products are : ",queryset.count())
#     serializer_class = ProductsSerializer







# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Products
# from products.serializers import ProductsSerializer

# class ProductListView(APIView):
#     def get(self, request):
#         session_id = request.session_id  # always available thanks to middleware

#         products = Products.objects.filter(is_active=True, vender__verified=True)[:10]
#         serializer = ProductsSerializer(products, many=True)

#         return Response({
#             'session_id': session_id,
#             'products': serializer.data
#         })
