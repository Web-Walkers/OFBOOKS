# Generated by Django 5.0.4 on 2024-07-15 10:31

import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='author_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='genre_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Interpreter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='interpreter_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='publishing_company_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='subject_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isbn', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='شابک')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('image', models.ImageField(upload_to='book_attachments')),
                ('material', models.CharField(choices=[('نرم', [('SMZ', 'شومیز'), ('KGZ', 'کاغذی'), ('SUN', 'نرم')]), ('سخت', [('CRM', 'چرمی'), ('PRC', 'پارچه\u200cای'), ('GLG', 'گالینگور'), ('HUN', 'سخت')])], max_length=4)),
                ('size', models.CharField(choices=[('RGH', 'رقعی'), ('VZR', 'وزیری'), ('NVZ', 'وزیری جدید'), ('PLT', 'پالتویی'), ('RHL', 'رحلی'), ('KST', 'خشتی'), ('JIB', 'جیبی')], default='VZR', max_length=4)),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('credit', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='book.author', verbose_name='نویسنده')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(related_name='books', to='book.genre')),
                ('interpreter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='book.interpreter', verbose_name='مترجم')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='book.publishing_company', verbose_name='انشارات')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='book.subject')),
            ],
        ),
    ]