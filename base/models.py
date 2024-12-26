from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class NavigationSettings(BaseGenericSetting):
    patreon_url = models.URLField(verbose_name="Patreon url", blank=True)
    youtube_url = models.URLField(verbose_name="YouTube url", blank=True)
    spotify_url = models.URLField(verbose_name="Spotify url", blank=True)
    apple_podcast_url = models.URLField(verbose_name="Apple Podcast url", blank=True)
    sound_cloud_url = models.URLField(verbose_name="SoundCloud url", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook url", blank=True)
    twitter_url = models.URLField(verbose_name="Twitter url", blank=True)
    mp3_url = models.URLField(verbose_name="MP3 url", blank=True)
    imdb_url = models.URLField(verbose_name="IMDB url", blank=True)
    rss_url = models.URLField(verbose_name="RSS feed url", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("patreon_url"),
                FieldPanel("youtube_url"),
                FieldPanel("spotify_url"),
                FieldPanel("apple_podcast_url"),
                FieldPanel("sound_cloud_url"),
                FieldPanel("facebook_url"),
                FieldPanel("twitter_url"),
                FieldPanel("mp3_url"),
                FieldPanel("rss_url"),
                FieldPanel("imdb_url"),
            ],
            "Podcast apps settings",
        )
    ]