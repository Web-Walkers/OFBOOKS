# Generated by Django 5.0.4 on 2024-07-21 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_order_predicted_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='predicted_date',
            new_name='saved_date',
        ),
    ]
