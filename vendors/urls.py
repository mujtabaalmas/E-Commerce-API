from django.urls import path
from .views import VendorListView #, BecomeVendorView

urlpatterns = [
    path('',VendorListView.as_view()),
    #path('become/', BecomeVendorView.as_view(), name='become-vendor'),
]