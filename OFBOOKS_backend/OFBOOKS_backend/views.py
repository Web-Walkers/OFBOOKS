from django.conf import settings

from django.shortcuts import redirect


def home(request):
    return redirect(settings.CORS_ALLOWED_ORIGINS[0])
    