# Generated by Django 5.0.4 on 2024-07-18 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_tag_options_tag_is_trend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'get_latest_by': '-is_trend', 'ordering': ['-is_trend'], 'verbose_name': 'هشتگ', 'verbose_name_plural': 'هشتگ ها'},
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('name',)},
        ),
    ]
