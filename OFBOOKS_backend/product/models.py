import uuid

from django.db import models
from django.conf import settings
from account.models import User

from django.utils.timesince import timesince

intab  = '1234567890'
outtab = '۱۲۳۴۵۶۷۸۹۰'
translation_table = str.maketrans(intab, outtab)

# --- Category ---
class Category(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255)

    def item_count(self):
        return self.products.count()

    def __str__(self) -> str:
        return self.name


# --- Product ---
class Product(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category    = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name        = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='product_attachments')
    description = models.TextField()
    height      = models.PositiveIntegerField()
    width       = models.PositiveIntegerField()

    credit      = models.DecimalField(max_digits=10, decimal_places=0)

    created_at  = models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='products', blank=False, null=True)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''
    
    def readable_credit(self):
        return f"{self.credit:,}".translate(translation_table)
    
    def created_at_formatted(self):

        return timesince(self.created_at).translate(translation_table) + " قبل"
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name