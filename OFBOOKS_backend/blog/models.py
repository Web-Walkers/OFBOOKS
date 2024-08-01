import uuid

from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings
import jdatetime
import datetime

from account.models import User

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

intab  = '1234567890'
outtab = '۱۲۳۴۵۶۷۸۹۰'
translation_table = str.maketrans(intab, outtab)


# --- Tag ---
class Tag(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255, verbose_name='نام')
    is_trend    = models.BooleanField(default=False, verbose_name='ترند')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        get_latest_by = '-is_trend'
        ordering = ["-is_trend"]
        verbose_name = _('هشتگ')
        verbose_name_plural = _('هشتگ ها')
        unique_together = ['name']


# --- Blog ---
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_posters', blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='blogs', verbose_name='هشتگ ها')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blogs', blank=False, null=True)

    def like_count(self):
        return self.likes.count()
    
    @property
    def is_liked(self):
        return 0

    def created_at_formatted(self):
        year, month, day = jdatetime.datetime.fromtimestamp(self.created_at.timestamp()).strftime('%Y %B %d').split()
        year, month = year[1:], months[month]
        if datetime.datetime.now().year == self.created_at.year:
            return f"{day} {month}".translate(translation_table)
        return f"{day} {month} {year}".translate(translation_table)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''
        
    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('مجله')
        verbose_name_plural = _('مجله ها')

    def __str__(self) -> str:
        return self.title


# --- Paragraph ---
class Paragraph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='paragraphs')
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('پاراگراف')
        verbose_name_plural = _('پاراگراف ها')
    
    def __str__(self) -> str:
        return '---------' if self.title == None else self.title


# --- Like ---
class Like(models.Model):
    created_by  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='likes', blank=False, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes', blank=False, null=False)

    class Meta:
        unique_together = [['created_by', 'created_for']]