# Generated by Django 5.1.4 on 2024-12-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpage_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
    ]
