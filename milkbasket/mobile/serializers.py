from rest_framework import serializers
from .models import Product, Customer, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category_id',
            'subcategory_id',
            'manufacturer_id',
            'selling_price_per_unit'
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'society_id',
            'city_id'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'customer_id',
            'product_id',
            'route_id',
            'store_id',
            'order_date',
            'product_quantity',
            'total_cost',
            'product_added_to_basket_on',
            'subscription'
        ]

class BPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'