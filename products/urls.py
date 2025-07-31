from django.urls import path 
#from .views import ProductListView
from .views import get_products_by_requests

urlpatterns = [
    # path('', ProductListView.as_view()),
    path('', get_products_by_requests, name='get_products_by_requests'),
]