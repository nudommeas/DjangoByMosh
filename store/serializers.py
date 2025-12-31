from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection, Review, Cart

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description', 'slug','inventory','unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculated_tax')
    def calculated_tax(self, product):
        return product.unit_price * Decimal(1.1)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = ['id', 'date', 'name', 'description']
     #We did not want to show the product, so we use the get_serializer_context method in the View and create method in the serializer.py

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id']