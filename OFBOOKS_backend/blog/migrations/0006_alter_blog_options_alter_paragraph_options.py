# Generated by Django 5.0.4 on 2024-07-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_at',), 'verbose_name': 'مجله', 'verbose_name_plural': 'مجله ها'},
        ),
        migrations.AlterModelOptions(
            name='paragraph',
            options={'ordering': ('created_at',), 'verbose_name': 'پاراگراف', 'verbose_name_plural': 'پاراگراف ها'},
        ),
    ]
