from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from users.views import RegisterView, LogoutView, CustomLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

