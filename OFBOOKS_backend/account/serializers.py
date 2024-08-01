from rest_framework import serializers

from .models import User, Address, Faaliat

class FaaliatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faaliat
        fields = (
            'detail',
            'link',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'biography',
            'get_avatar',
            'is_staff',
            'is_premium',
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'name',
            'phone',
            'province',
            'city',
            'address',
            'get_full_address',
            'zip_code',
        )