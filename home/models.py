from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from blog.models import BlogIndexPage, BlogPage
from podcast.models import EpisodeIndexPage, EpisodePage


class HomePage(Page):

    def get_context(self, request):
        context = super().get_context(request)
        blog_index = BlogIndexPage.objects.live().first()
        if blog_index:
            recent_blog_posts = BlogPage.objects.child_of(blog_index).live().order_by('-date')[:3]
        else:
            recent_blog_posts = []

        episode_index = EpisodeIndexPage.objects.live().first()
        if episode_index:
            recent_episodes = EpisodePage.objects.child_of(episode_index).live().order_by('-date')[:3]
        else:
            recent_episodes = []

        context['recent_blog_posts'] = recent_blog_posts
        context['recent_episodes'] = recent_episodes
        context['blog_index'] = blog_index
        context['episode_index'] = episode_index
        return context
