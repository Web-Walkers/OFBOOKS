from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Paragraph, Blog

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'name',
#             'password1',
#             'password2',
#         )

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = (
#             'name',
#             'biography',
#             'avatar',
#         )