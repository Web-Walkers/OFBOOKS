# Generated by Django 5.0.4 on 2024-07-15 21:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_genres_alter_book_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-created_at',), 'verbose_name': 'کتاب', 'verbose_name_plural': 'کتاب ها'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'کتاب', 'verbose_name_plural': 'کتاب ها'},
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default='', verbose_name='توضیحات'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='ادمین'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subject_pictures', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
    ]
