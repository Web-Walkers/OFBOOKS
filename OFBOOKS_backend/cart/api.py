from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User, Faaliat
from account.serializers import UserSerializer

# from .forms 
from .models import Order, OrderItem, PaymentDetails, Address
from book.models import Book
from product.models import Product
from .serializers import OrderSerializer

from  datetime import datetime


@api_view(['GET'])
def get_cart(request):
    user = User.objects.get(pk=request.user.id)

    order, _ = Order.objects.get_or_create(
        created_by = user, 
        is_ordered = False,
    )

    order_serializer = OrderSerializer(order)

    return JsonResponse(order_serializer.data, safe=False)


@api_view(['POST'])
def add_to_cart(request):
    user = User.objects.get(pk=request.user.id)
    data = request.data
    message = 'success'

    if data.get('type') == 'book':
        order_item, status = OrderItem.objects.get_or_create(
            created_by = user, 
            is_ordered = False,
            product_id = data.get('id'),
            product_type = ContentType.objects.get_for_model(Book)
        )
    elif data.get('type') == 'non-book':
        order_item, status = OrderItem.objects.get_or_create(
            created_by = user, 
            is_ordered = False,
            product_id = data.get('id'),
            product_type = ContentType.objects.get_for_model(Product)
        )
    else:
        return JsonResponse({'message' : 'مقادیر نادرست هستند', 'status':'false'}, status=500)

    if status:
        order, status = Order.objects.get_or_create(
            created_by = user, 
            is_ordered = False,
        )
        order.items.add(order_item)
        order.save()
    else:
        order_item.quantity += 1
        order_item.save()

    if message == 'success':
        detail = f"{'کتاب' if data.get('type') == 'book' else ''} {order_item} به سبد خرید اضافه شد"
        link = '/my-cart'
        action = Faaliat(detail=detail, link=link, created_by=request.user)
        action.save() 
    
    return JsonResponse({'message': message}, safe=False)


@api_view(['POST'])
def set_quantity(request):
    user = User.objects.get(pk=request.user.id)
    order_item = OrderItem.objects.get(pk=request.data.get('order_item_id'))

    new_quantity = request.data.get('new_quantity')

    if new_quantity > 0 :
        order_item.quantity = new_quantity
        order_item.save(update_fields=['quantity'])

    else :
        order_item.delete()

    order = Order.objects.get(
        created_by = user, 
        is_ordered = False,
    )
        
    order_serializer = OrderSerializer(order)
    return JsonResponse(order_serializer.data, safe=False)


@api_view(['POST'])
def set_address(request, id):
    user = request.user
    data = request.data
    message = 'success'

    order = Order.objects.get(pk=id)

    assert user.id == order.created_by.id

    order.address = Address.objects.get(pk=data.get('checkedAddress'))
    order.description = data.get('description')
    order.save()

    return JsonResponse({'message': message}, safe=False)


@api_view(['GET'])
def get_cart_(request, id):
    order = Order.objects.get(pk=id)

    assert order.created_by.id == request.user.id

    order_serializer = OrderSerializer(order)

    return JsonResponse(order_serializer.data, safe=False)


@api_view(['GET']) # TODO: Fix all of it...
def order(request, id):
    user = request.user
    message = 'success'

    order = Order.objects.get(pk=id)

    assert user.id == order.created_by.id
    assert order.is_ordered == False
    assert len(order.get_cart_items()) > 0

    order.is_ordered = True
    order.saved_date = datetime.today()
    order.save()

    for item in OrderItem.objects.filter(created_by=user, is_ordered=False, order=order):
        item.set_is_ordered()

    if message == 'success':
        detail = f"سفارش شما با کد پبگیری {order.id} درحال بررسی است"
        link = f'/done/{order.id}'
        action = Faaliat(detail=detail, link=link, created_by=user)
        action.save() 

    return JsonResponse({'message': message}, safe=False)


@api_view(['GET'])
def get_history(request):
    orders = Order.objects.filter(created_by=request.user, is_ordered=True)

    orders_serializer = OrderSerializer(orders, read_only=True, many=True)

    return JsonResponse(orders_serializer.data, safe=False)