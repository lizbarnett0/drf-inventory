from rest_framework import serializers
from .models import Category, Vendor, Product, ProductInstance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'products')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'products')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    vendor = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name',
                  'vendor', 'description', 'model', 'category')


class ProductInstanceSerializer(serializers.ModelSerializer):
    product = CategorySerializer(read_only=True)

    class Meta:
        model = ProductInstance
        fields = ('id', 'uuid',
                  'purchase_date', 'sold_date', 'cost', 'model', 'product')
