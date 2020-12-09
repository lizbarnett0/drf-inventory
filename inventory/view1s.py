from django.shortcuts import render
from rest_framework import viewsets  # <- import viewsets
from .models import Book, Author  # <- don't forget your models
from .serializers import ProductSerializer, ProductInstanceSerializer, CategorySerializer, VendorSerializer  # <- or serializers

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer


class ProductInstanceViewSet(viewsets.ModelViewSet):
    queryset = ProductInstance.objects.all()
    serializer_class = ProductInstanceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

