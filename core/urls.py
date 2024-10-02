from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    # Example route
    path('', views.home, name='home'),  # Replace with your actual views
]