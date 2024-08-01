from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('profile/<uuid:id>/', api.get_profile, name='profile'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editprofile/', api.editprofile, name='edit_profile'),
    path('address/', api.address, name='address'),
    path('addresses/', api.addresses, name='addresses'),
    path('recent-actions/<int:idx>/', api.recent_actions, name='recent_actions'),
]