from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import redirect

from .models import User


def activateemail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id', '')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()

        return redirect(
            f'{settings.CORS_ALLOWED_ORIGINS[0]}/register'
        )
    else:
        return HttpResponse('The parameters is not valid!')
    