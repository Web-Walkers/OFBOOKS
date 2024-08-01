from django.contrib import admin

from .models import User, Address, Faaliat

@admin.register(User)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'is_staff', 'is_premium', 'is_superuser', 'is_active')

admin.site.register(Address)
admin.site.register(Faaliat)