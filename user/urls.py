from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    # Example route
    path('login/', views.login_view, name="login"),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),  # Replace with your actual views
]