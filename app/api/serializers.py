from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Customers,Products,Orders,Reviews


class CustomersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customers
       fields = ['CustomersID', 'FirstName', 'LastName']

   def validate(self, attrs):
       unknown = set(self.initial_data) - set(self.fields)
       if unknown:
           raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
       return attrs



class ProductsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Products
       fields = ['ProductID', 'Name', 'Price']

   def validate(self, attrs):
       unknown = set(self.initial_data) - set(self.fields)
       if unknown:
           raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
       return attrs


class OrdersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Orders
       fields = ['OrdersID', 'Customers_ID', 'Product_ID','Quantity','CreatedAt']

   def validate(self, attrs):
       unknown = set(self.initial_data) - set(self.fields)
       if unknown:
           raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
       return attrs

class ReviewsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reviews
       fields = ['ReviewID', 'Customers_ID', 'Product_ID','Rating','Review']

   def validate(self, attrs):
       unknown = set(self.initial_data) - set(self.fields)
       if unknown:
           raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
       return attrs
