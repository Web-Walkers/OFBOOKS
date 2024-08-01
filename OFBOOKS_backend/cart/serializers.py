from rest_framework import serializers

from .models import Order, OrderItem, PaymentDetails
from book.models import Book
from product.models import Product

from account.serializers import UserSerializer, AddressSerializer
from book.serializers import BookSerializer
from product.serializers import ProductSerializer


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Book):
            serializer = BookSerializer(value)
        elif isinstance(value, Product):
            serializer = ProductSerializer(value)
        else:
            raise Exception('Unexpected type of item object')
        
        return serializer.data


class OrderItemSerializer(serializers.ModelSerializer):
    product_object = ItemRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id', 
            'product_object',
            'product_type',
            'get_readable_credit',
            'quantity', 
        ]


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    items = OrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order
        fields = [
            'id', 
            'items',
            'get_predicted_date', 
            'get_readable_credit',
            'get_cart_total',
            'address',
            'is_sent',
        ]