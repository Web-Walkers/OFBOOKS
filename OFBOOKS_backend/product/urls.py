from django.urls import path

from . import api

urlpatterns = [
    path('', api.get_feed, name='get_feed'),
    path('categories/', api.get_categories, name='get_categories'),
    path('<uuid:id>/', api.product_detail, name='product_detail'),
]