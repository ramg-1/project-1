from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('recommended/', views.recommended_properties, name='recommended_properties'),
    path('add-property/', views.add_property, name='add_property'),  # Add this line
]