# Generated by Django 5.0.4 on 2024-07-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_sub_title_paragraph_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
