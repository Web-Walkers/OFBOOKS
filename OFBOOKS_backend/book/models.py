import uuid
from isbn_field import ISBNField
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.conf import settings
from account.models import User
from blog.models import Tag


# --- Achievement ---
class Achievement(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('افتخار')
        verbose_name_plural = _('افتخارات')


# --- Genre ---
class Genre(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='genre_pictures', blank=True, null=True)

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('ژانر')
        verbose_name_plural = _('ژانرها')
    

# --- Subject ---
class Subject(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255, verbose_name='نام')
    image       = models.ImageField(upload_to='subject_pictures', blank=True, null=True, verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('دسته بندی موضوعی')
        verbose_name_plural = _('موضوعات')
    

# --- Literature ---
class Literature(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255, verbose_name='نام')
    image       = models.ImageField(upload_to='international_pictures', blank=True, null=True, verbose_name='تصویر')
    description = models.TextField(blank=True, verbose_name='توضیحات')

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('ادبیه ملت')
        verbose_name_plural = _('ادبیات ملل')
    
    @classmethod
    def get_default_pk(cls):
        literature, created = cls.objects.get_or_create(
            name='default value', 
            defaults=dict(description='this is not an real value'),
        )
        return literature.pk


# --- Author ---
class Author(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='author_pictures', blank=True, null=True)
    description = models.TextField(verbose_name='درباره نویسنده')

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('نویسنده')
        verbose_name_plural = _('نویسندگان')
    

# --- Interpreter ---
class Interpreter(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='interpreter_pictures', blank=True, null=True)

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('مترجم')
        verbose_name_plural = _('مترجمین')


# --- Publishing Company ---
class Publishing_Company(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='publishing_company_pictures', blank=True, null=True)
    description = models.TextField(verbose_name='توضیحات', default='توضیحات')

    def item_count(self):
        return self.books.count()

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('نشریه')
        verbose_name_plural = _('ناشرین')


# --- BOOK ---
class Book(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn            = ISBNField(verbose_name='شابک')
    name            = models.CharField(max_length=255, verbose_name='نام')
    author          = models.ForeignKey(Author, related_name='books', on_delete=models.PROTECT, verbose_name='نویسنده')
    interpreter     = models.ForeignKey(Interpreter, related_name='books', on_delete=models.PROTECT, blank=True, null=True, verbose_name='مترجم')
    publisher       = models.ForeignKey(Publishing_Company, related_name='books', on_delete=models.PROTECT, verbose_name='انشارات')
    image           = models.ImageField(upload_to='book_attachments')

    class Size(models.TextChoices):
        """ Book Sizes """
        RGH = "RGH", _("رقعی")        #   |   ۱۴۱ × ۲۱۲   |
        VZR = "VZR", _("وزیری")       #   |   ۱۶۵ × ۲۳۵   |
        NVZ = "NVZ", _("وزیری جدید")  #   |   ۱۶۵ × ۲۱۲   |
        PLT = "PLT", _("پالتویی")     #   |   ۱۲۵ × ۲۰۰   |
        RHL = "RHL", _("رحلی")        #   |   ۲۱۰ × ۲۸۰   |
        KST = "KST", _("خشتی")        #   |   ۲۲۰ × ۲۲۰   |
        JIB = "JIB", _("جیبی")        #   |   ۱۱۵ × ۱۶۵   |
        # (...)

    MATERIAL_CHOICES = (
        ('نرم', (
                ('SMZ', 'شومیز'),
                ('KGZ', 'کاغذی'),
                ('SUN', 'نرم'),
            )
        ),
        ('سخت', (
                ('CRM', 'چرمی'),
                ('PRC', 'پارچه‌ای'),
                ('GLG', 'گالینگور'),
                ('HUN', 'سخت'),
            )
        ),
    )

    material = models.CharField(
        max_length=4,
        choices=MATERIAL_CHOICES,
    )

    size = models.CharField(
        max_length=4,
        choices=Size.choices,
        default=Size.VZR,
    )

    height = models.PositiveIntegerField(blank=True, null=True)
    width  = models.PositiveIntegerField(blank=True, null=True)
    pages  = models.PositiveIntegerField()

    tags        = models.ManyToManyField(Tag, related_name='books', blank=True, verbose_name='هشتگ ها')
    genres      = models.ManyToManyField(Genre, related_name='books', verbose_name='ژانر')
    subject     = models.ForeignKey(Subject, related_name='books', on_delete=models.PROTECT, verbose_name='دسته بندی موضوعی')
    literature  = models.ForeignKey(Literature, related_name='books', on_delete=models.PROTECT, blank=True, null=True, verbose_name='ادبیات ملل')

    
    introduction= models.TextField(verbose_name='معرفی کتاب')
    achievements= models.ManyToManyField(Achievement, related_name='books', blank=True, verbose_name='افتخارات کتاب')

    credit      = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')

    created_at  = models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='books', verbose_name='ادمین', blank=False, null=True)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''
    
    def readable_credit(self):
        return f"{self.credit:,}".translate(str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰'))
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('کتاب')
        verbose_name_plural = _('کتاب ها')

    def __str__(self) -> str:
        return self.name
    


"""
               `           '
                `         '
                 :       :
___              `       '              ___
`Y8888ba.         :     :         .ad8888P'
  88888888b.      `     '      .d88888888
  8888888888b.     :   :     .d8888888888
  88888P'  `?8b.   `   '   .d8P'  `?88888
  88888       "8b   : :   d8"       88888
 j88888  .db.   ?b       dP   .db.  88888k
   `888  8888    `b ( ) d'    8888  888'
    888. ?88P                 ?88P .888
    8888  ""        / \        ""  8888
    8888b.   _,aaY' | | `Yaa,_   .d8888
   j8888888888f"'   \ /    `"?888888888k
      88888'.'      d b       `.`8888
      88' .8       d' `b       8. `88
      f  .88 db   d'| |`b   db 88.  l
         888 `'   8 | | 8   `' 88b
         888      8 | | 8      888
        d888b   .d8 \_/ 8b.   d888b
        88888888888     88888888888
        8888888888       8888888888
        f 8888888'       `8888888 l
          `888888         888888'
           8P  `Y         Y'  ?8
           8                   8
           f                   l
"""