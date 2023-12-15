from django.urls import path,re_path,include
from  .views import Customers_list

urlpatterns = [
path('Customers_list/',Customers_list,name='Customers_list')
]
