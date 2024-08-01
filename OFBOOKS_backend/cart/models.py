from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html

import uuid

from django.db import models
from django.conf import settings
import jdatetime
from  datetime import datetime, timedelta

from account.models import User, Address

months = {
    'Farvardin':'فروردین',
    'Ordibehesht':'اردیبهشت',
    'Khordad':'خرداد',
    'Tir':'تیر',
    'Mordad':'مرداد',
    'Shahrivar':'شهریور',
    'Mehr':'مهر',
    'Aban':'آبان',
    'Azar':'آذر',
    'Dey':'دی',
    'Bahman':'بهمن',
    'Esfand':'اسفند',
}

# --- Payment Details ---
class PaymentDetails(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount      = models.DecimalField(max_digits=13, decimal_places=0, verbose_name='مقدار')
    provider    = models.CharField(max_length=50)
    status      = models.CharField(max_length=50)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='payments', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_readable_credit(self):
        return f"{self.amount:,}".translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰'))

    class Meta:
        verbose_name = _('جزئیات پرداخت')
        verbose_name_plural = _('جزئیات پرداخت ها')


# --- Order Item ---
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    product_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    product_id      = models.UUIDField()
    product_object  = GenericForeignKey('product_type', 'product_id')

    quantity = models.PositiveSmallIntegerField(_("تعداد"), default=1)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order_items', blank=False, null=True, verbose_name='سفارش دهنده')
    created_at = models.DateTimeField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False, verbose_name=_("ثبت سفارش"))
    ordered_at = models.DateTimeField(blank=True, null=True)

    def set_is_ordered(self):
        self.is_ordered = False if self.order.first() == None else self.order.first().is_ordered
        self.save()

    def get_cart_total(self):
        return self.product_object.credit * self.quantity
    
    def get_readable_credit(self):
        return f"{self.get_cart_total():,}".translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰'))

    class Meta:
        verbose_name = _('کالا')
        verbose_name_plural = _('کالا ها')

    def __str__(self):
        prefix = 'کتاب ' if str(self.product_type).startswith('کتاب') else ''
        return f"\n{self.quantity} عدد {prefix}{self.product_object} با کد ({self.product_id})"


# --- Order ---
class Order(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    items      = models.ManyToManyField(OrderItem, related_name='order', verbose_name=_("کالا ها"))
    is_ordered = models.BooleanField(default=False, verbose_name=_("ثبت سفارش"))
    is_sent = models.BooleanField(default=False, verbose_name=_("وضعیت ارسال"))
    payment_details = models.OneToOneField(PaymentDetails, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('جزئیات پرداخت'), related_name='order')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('گیرنده'), related_name='order')
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    saved_date = models.DateTimeField(blank=True, null=True)

    def get_predicted_date(self):
        if self.saved_date:
            d = self.saved_date
        else:
            d = datetime.today() + timedelta(days=4)
        month, day = jdatetime.datetime.fromtimestamp(
            d.timestamp()
        ).strftime('%B %d').split()
        return f"{day} {months[month]}".translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰'))
    
    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum([item.product_object.credit * item.quantity for item in self.items.all()])
    
    def get_readable_credit(self):
        return f"{self.get_cart_total():,}".translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰'))
    
    def __str__(self) -> str:
        return f"{self.created_by} - {self.id}"
        
    class Meta:
        ordering = ('-is_ordered', 'is_sent', 'updated_at',)
        verbose_name = _('سفارش')
        verbose_name_plural = _('سفارشات')