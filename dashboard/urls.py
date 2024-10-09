from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    
    path('user-menu/', views.dashboard, name="dashboard"),
    path('request-details/<int:id>/', views.user_request_detail, name='request-details'),
]