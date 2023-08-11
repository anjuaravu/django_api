from django.contrib import admin
from .models import Products,Customer_preference,Orders

# Register your models here.

admin.site.register(Products)
admin.site.register(Customer_preference)
admin.site.register(Orders)