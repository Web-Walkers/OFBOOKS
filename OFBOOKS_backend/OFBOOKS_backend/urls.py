from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home
from account.views import activateemail

admin.site.index_title = "آف بوکز"
admin.site.site_title = "درگاه مدیریت آف بوکز"

urlpatterns = [
    path('', home, name='index'),
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/blogs/', include('blog.urls')),
    path('api/products/', include('product.urls')),
    path('api/books/', include('book.urls')),
    path('api/cart/', include('cart.urls')),
    path('activateemail/', activateemail, name='activate email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)