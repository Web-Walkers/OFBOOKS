from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer

# from .forms 
from .models import Category, Product
from .serializers import CategorySerializer, \
                            ProductSerializer, \
                            ProductDetailSerializer


@api_view(['GET'])
@permission_classes([])
def get_categories(request):
    category = Category.objects.all()
    
    category_serializer = CategorySerializer(category, many=True)

    return JsonResponse(category_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([])
def get_feed(request):
    data = request.data
    category_id, sort_by, idx = data['category_id'], data['sort_by'], data['idx']

    if category_id:
        category = Category.objects.get(pk=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    
    match sort_by:
        case 'new':
            products = products.order_by('-created_at')
        case 'low_price':
            products = products.order_by('credit')
        case 'high_price':
            products = products.order_by('-credit')
        case 'bestseller':
            ...
        case 'view':
            ...

    products = products[0:idx + 6 if idx==0 else idx + 12]
    
    products_serializer = ProductSerializer(products, many=True)

    return JsonResponse(products_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    
    product_serializer = ProductDetailSerializer(product)

    return JsonResponse({
        'product': product_serializer.data,
    }, safe=False)
    
