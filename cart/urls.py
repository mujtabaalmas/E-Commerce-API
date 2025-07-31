
from django.urls import path
from .views import AddToCartView, CartView

urlpatterns = [
    path('cart/add/', AddToCartView.as_view()),
    path('cart/', CartView.as_view()),
]
