# Generated by Django 5.1.4 on 2024-12-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_navigationsettings_apple_podcast_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationsettings',
            name='facebook_url',
            field=models.URLField(blank=True, verbose_name='Facebook url'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='imdb_url',
            field=models.URLField(blank=True, verbose_name='IMDB url'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='mp3_url',
            field=models.URLField(blank=True, verbose_name='MP3 url'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='patreon_url',
            field=models.URLField(blank=True, verbose_name='Patreon url'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='rss_url',
            field=models.URLField(blank=True, verbose_name='RSS feed url'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='twitter_url',
            field=models.URLField(blank=True, verbose_name='Twitter url'),
        ),
    ]
