from rest_framework import serializers
from .models import Products,Customer_preference,Orders

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Products
        fields=['product_id','product_name','product_price']


class Customer_preferenceSerializer(serializers.HyperlinkedModelSerializer):
    product_id=ProductsSerializer()
    class Meta:
        model=Customer_preference
        fields=['preference_id','product_id']


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    preference_id=Customer_preferenceSerializer()
    class Meta:
        model=Orders
        fields=['customer_id','preference_id','order_date']