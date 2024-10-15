
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    # Example route
    path('login/', views.login_view, name="login"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),  # Replace with your actual views
]



  