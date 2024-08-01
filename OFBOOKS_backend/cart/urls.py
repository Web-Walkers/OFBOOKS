from django.urls import path

from . import api

urlpatterns = [
    path('', api.get_cart, name='get_cart'),
    path('<uuid:id>/', api.get_cart_, name='get_cart'),
    path('add/', api.add_to_cart, name='add_to_cart'),
    path('set-quantity/', api.set_quantity, name='set_quantity'),
    path('set-address/<uuid:id>/', api.set_address, name='set_address'),
    path('order/<uuid:id>/', api.order, name='order'),
    path('get-history/', api.get_history, name='get_history'),
]