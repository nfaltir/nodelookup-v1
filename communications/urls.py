from django.urls import path
from . import views  # Assuming you have views in the same app

urlpatterns = [
    path('user-communications/messages/', views.inbox, name='inbox'),  
    path('user-communications/send-message/', views.send_message, name='send-message'),
]