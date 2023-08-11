from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Products, Customer_preference, Orders
from .serializers import ProductsSerializer, Customer_preferenceSerializer, OrdersSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Customer_preferenceViewSet(viewsets.ModelViewSet):
    queryset = Customer_preference.objects.all()
    serializer_class = Customer_preferenceSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class ProductApiView(APIView):
#     def get(self,request):
#         allProducts=Products.objects.all().values()
#         return Response({"Message":"Products","Product List":allProducts})
















