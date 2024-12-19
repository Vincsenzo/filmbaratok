# Generated by Django 5.1.4 on 2024-12-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_url', models.URLField(blank=True, verbose_name='YouTube url')),
                ('spotify_url', models.URLField(blank=True, verbose_name='Spotify url')),
                ('sound_cloud_url', models.URLField(blank=True, verbose_name='SoundCloud url')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]