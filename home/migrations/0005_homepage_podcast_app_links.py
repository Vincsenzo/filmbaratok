# Generated by Django 5.1.4 on 2024-12-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_recent_blogs_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='podcast_app_links',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]