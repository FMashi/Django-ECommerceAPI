from django.contrib import admin

# Register your models here.

from .models import Customers,Products,Orders,Reviews

# Register your models here.
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Reviews)

