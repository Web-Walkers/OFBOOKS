from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, Address

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'password1',
            'password2',
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name',
            'biography',
            'avatar',
        )

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'name',
            'phone',
            'province',
            'city',
            'address',
            'zip_code',
        )