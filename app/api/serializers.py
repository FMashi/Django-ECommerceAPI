from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Customer, Product, Order, Review

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'quantity', 'created_at']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'product', 'rating', 'review']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data
