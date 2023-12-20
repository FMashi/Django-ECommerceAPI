from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, 
    CustomerViewSet, 
    OrderViewSet, 
    ReviewViewSet,
    register_user,
    user_login,
    user_logout)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
