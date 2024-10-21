from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('pricing/', views.pricing, name='pricing'),
    path('gallery/', views.gallery, name='gallery'),
    path('product/', views.product, name='product'),
]