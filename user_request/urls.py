from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    
    path('user-request/', views.user_request, name="user-request"),
    path('request-success/', views.request_success, name="request-success"),
]