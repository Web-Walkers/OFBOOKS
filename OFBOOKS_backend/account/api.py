from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core import mail
from django.template.loader import render_to_string
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm, ProfileForm, AddressForm
from .serializers import UserSerializer, AddressSerializer, FaaliatSerializer
from .models import User, Address, Faaliat


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'biography': request.user.biography,
        'email': request.user.email,
        'avatar': request.user.get_avatar(),
        'isStaff': request.user.is_staff,
        'isPremium': request.user.is_premium,
    })


@api_view(['GET'])
@permission_classes([])
def get_profile(request, id):
    user = User.objects.get(pk=id)
    user_serializer = UserSerializer(user)

    url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

    subject = "آف بوکز"
    html_message = render_to_string('email_activation.html', {'ACTIVATION_URL': url})
    from_email = 'From <ofbooks403@gmail.com>'
    to = [user.email]

    email = mail.EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=to,
    )
    email.content_subtype = 'html'
    email.send()
    
    return JsonResponse({
        'user': user_serializer.data,
    }, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = False  
        user.save()

        url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        subject = "لطفاً احراز هویت را تکمیل کنید"
        html_message = render_to_string('email_activation.html', {'ACTIVATION_URL': url})
        from_email = 'From <ofbooks403@gmail.com>'
        to = [user.email]

        email = mail.EmailMessage(
            subject=subject,
            body=html_message,
            from_email=from_email,
            to=to,
        )
        email.content_subtype = 'html'
        email.send()
        

    else:
        message = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)


@api_view(['POST'])
def editprofile(request):
    user = request.user

    form = ProfileForm(
        request.POST,
        request.FILES,
        instance=user,
    )
    if form.is_valid():
        form.save()

    serializer = UserSerializer(user)

    return JsonResponse({
        'message': 'successful',
        'user': serializer.data,
    })


@api_view(['GET'])
def addresses(request):
    my_addresses = request.user.addresses
    addresses_serializer = AddressSerializer(my_addresses, read_only=True, many=True)
    
    return JsonResponse(addresses_serializer.data, safe=False)


@api_view(['POST'])
def address(request):
    id = request.data.get('id')

    if id == 'new':
        form = AddressForm(
            request.data.get('form'),
        )

    else:
        my_address = Address.objects.get(pk=id)
        form = AddressForm(
            request.data.get('form'),
            instance=my_address,
        )

    if form.is_valid():
        my_address = form.save()
        my_address.created_by = request.user
        my_address.created_by = request.user
        my_address.save()
    
    else:
        return JsonResponse({'status':'false'}, status=500)
    
    
    my_addresses = request.user.addresses
    addresses_serializer = AddressSerializer(my_addresses, read_only=True, many=True)
    
    return JsonResponse(addresses_serializer.data, safe=False)


@api_view(['GET'])
def recent_actions(request, idx):
    faaliatha = Faaliat.objects.filter(created_by=request.user)[:idx+4]
    print(idx)
    faaliatha_serializer = FaaliatSerializer(faaliatha, read_only=True, many=True)
    
    return JsonResponse(faaliatha_serializer.data, safe=False)

