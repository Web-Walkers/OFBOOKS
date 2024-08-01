from django.contrib import admin

from .models import OrderItem, Order, PaymentDetails

admin.site.register(PaymentDetails)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_ordered', 'is_sent', 'item_count', 'readable_credit',)
    readonly_fields = ['items', 'is_ordered', 'payment_details', 'address', 'description', 'created_by', 'created_at', 'updated_at', 'saved_date']

    list_editable = ['is_sent']

    def readable_credit(self, obj):
        return obj.get_readable_credit()
    readable_credit.short_description = 'قیمت'

    def item_count(self, obj):
        return sum([item.quantity for item in obj.items.all()])
    item_count.short_description = 'تعداد محصولات سفارش داده شده'

    def items_(self, obj):
        return obj.items.get_url()
    items_.short_description = 'سفارشات'

    include = ['items_',]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by', 'is_ordered_',)

    def is_ordered_(self, obj):
        obj.set_is_ordered()
        return obj.is_ordered
    is_ordered_.short_description = "ثبت سفارش"
    is_ordered_.boolean = True
