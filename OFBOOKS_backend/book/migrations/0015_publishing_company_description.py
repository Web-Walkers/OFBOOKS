# Generated by Django 5.0.4 on 2024-07-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_book_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishing_company',
            name='description',
            field=models.TextField(default='توضیحات', verbose_name='توضیحات'),
        ),
    ]