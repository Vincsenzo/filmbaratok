# Generated by Django 5.1.4 on 2024-12-04 20:45

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.author'),
        ),
    ]
