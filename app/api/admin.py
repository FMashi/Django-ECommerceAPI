from django.contrib import admin
from .models import CustomUser, Customer, Product, Order, Review

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'created_at')
    search_fields = ('customer__first_name', 'product__name')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'rating')
    search_fields = ('customer__first_name', 'product__name')
    list_filter = ('rating',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(CustomUser)
