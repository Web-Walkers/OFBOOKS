# Generated by Django 5.0.4 on 2024-07-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='predicted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]