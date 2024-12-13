from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class NavigationSettings(BaseGenericSetting):
    youtube_url = models.URLField(verbose_name="YouTube url", blank=True)
    spotify_url = models.URLField(verbose_name="Spotify url", blank=True)
    apple_podcast_url = models.URLField(verbose_name="Apple Podcast url", blank=True)
    sound_cloud_url = models.URLField(verbose_name="SoundCloud url", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("youtube_url"),
                FieldPanel("spotify_url"),
                FieldPanel("apple_podcast_url"),
                FieldPanel("sound_cloud_url"),
            ],
            "Podcast apps settings",
        )
    ]