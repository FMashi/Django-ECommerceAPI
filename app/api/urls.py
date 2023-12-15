from django.urls import path,re_path,include
from  .views import Customers_list

urlpatterns = [
path('article_list/',Customers_list,name='article_list')
]
