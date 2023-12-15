from django.urls import path
from .views import (
    CustomerListCreateView, CustomerRetrieveUpdateDestroyView,

)

urlpatterns = [
    # Customer URLs
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),
    
    # Product URLs
    
    # Order URLs

    # Review URLs
    
]
