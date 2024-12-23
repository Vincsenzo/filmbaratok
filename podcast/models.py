from django.db import models
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalManyToManyField

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.search import index


class EpisodeIndexPage(Page):

    def get_context(self, request):
        context = super().get_context(request)
        episode_pages_all = EpisodePage.objects.child_of(self).live().order_by('-date')
        paginator = Paginator(episode_pages_all, 12)

        page = request.GET.get('page')
        try:
            episode_pages = paginator.page(page)
            episode_pages.adjusted_elided_pages = paginator.get_elided_page_range(page, on_each_side=1, on_ends=0)
        except PageNotAnInteger:
            episode_pages = paginator.page(1)
            episode_pages.adjusted_elided_pages = paginator.get_elided_page_range(1, on_each_side=1, on_ends=0)
        except EmptyPage:
            episode_pages = paginator.page(paginator.num_pages)
            episode_pages.adjusted_elided_pages = paginator.get_elided_page_range(paginator.num_pages, on_each_side=1, on_ends=0)

        context['episode_pages'] = episode_pages
        return context


class EpisodePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    duration = models.DurationField()
    authors = ParentalManyToManyField('blog.Author', blank=True)
    authors_old = models.CharField(max_length=250, blank=True, null=True)
    cover_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    youtube_url = models.URLField(verbose_name="YouTube url", blank=True)
    spotify_url = models.URLField(verbose_name="Spotify url", blank=True)
    apple_podcast_url = models.URLField(verbose_name="Apple Podcast url", blank=True)
    sound_cloud_url = models.URLField(verbose_name="SoundCloud url", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('duration', widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'})), #TODO: make this work
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('cover_image'),
        MultiFieldPanel([
            FieldPanel('youtube_url'),
            FieldPanel('spotify_url'),
            FieldPanel('apple_podcast_url'),
            FieldPanel('sound_cloud_url'),
        ], heading="Episode links"),
    ]