from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        ) 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'get_image',
            'readable_credit',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'created_by',
            'created_at_formatted',
            'get_image',
            'height',
            'width',
            'readable_credit',
        )