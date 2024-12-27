import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from wagtail.models import Page
from podcast.models import EpisodePage, EpisodeIndexPage
from wagtail.images.models import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from datetime import datetime, date
from .data_utils import get_sound_data, replace_links_with_anchors

class Command(BaseCommand):
    help = 'Fetch the latest episodes from the RSS feed and update the database'

    def handle(self, *args, **options):
        url = "https://feeds.soundcloud.com/users/soundcloud:users:261242545/sounds.rss"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write(f"Failed to fetch RSS feed. HTTP status code: {response.status_code}")
            return

        rss_feed = response.text
        root = ET.fromstring(rss_feed)
        namespaces = {
            'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
            'atom': 'http://www.w3.org/2005/Atom',
        }

        # Saving the one repeating image outside of the loop
        multy_image_url = "https://i1.sndcdn.com/artworks-000277146878-d4b788-t500x500.jpg"
        multy_image_title = "Filmbaratok"
        response = requests.get(multy_image_url)
        image_data = BytesIO(response.content)
        multy_wagtail_image = Image(title=multy_image_title)
        multy_wagtail_image.file = InMemoryUploadedFile(image_data, None, multy_image_title + '.jpg', 'image/jpeg', len(response.content), None)
        multy_wagtail_image.save()

        for item in root.findall('./channel/item'):
            title = item.findtext('title')

            # Check if an episode already exists
            if EpisodePage.objects.filter(title=title).exists():
                # self.stdout.write(f"Episode '{title}' already exists. Skipping.")
                continue

            pub_date_raw = item.findtext('pubDate')
            pub_date = datetime.strptime(pub_date_raw, '%a, %d %b %Y %H:%M:%S %z').date()
            link = item.findtext('link')
            duration = item.findtext('itunes:duration', namespaces=namespaces)
            # description = item.findtext('description')
            audio_link = item.find('./enclosure').attrib.get('url') if item.find('./enclosure') is not None else None
            image_link = item.find('itunes:image', namespaces=namespaces).attrib.get('href') if item.find('itunes:image', namespaces=namespaces) is not None else None

            response_img = None
            wagtail_image = None
            reference_date = date(2017, 12, 29)

            if pub_date < reference_date:
                wagtail_image = multy_wagtail_image
            else:            
                if image_link:
                        image_link = image_link.replace("t3000x3000", "t500x500")
                        response_img = requests.get(image_link)
                        if response_img.status_code == 200:
                            image_data = BytesIO(response_img.content)
                            wagtail_image = Image(title=title)
                            wagtail_image.file = InMemoryUploadedFile(image_data, None, f"{title}.jpg", 'image/jpeg', len(response_img.content), None)
                            wagtail_image.save()
                else:
                    self.stdout.write(f"No image link found for episode '{title}'. Skipping image download.")

            description = None
            artists = None
            description, artists = get_sound_data(link)
            intro_text = description[:150] + "..." if description else ""
            if description:
                description = replace_links_with_anchors(description)
                description = description.replace('\n', '<br/>')

            # Create a new episode
            parent_page = EpisodeIndexPage.objects.first()
            episode_page = EpisodePage(
                title=title,
                date=pub_date,
                intro=intro_text,
                body=description,
                duration=duration,
                authors_old=artists,
                sound_cloud_url=link,
                audio_direct_url=audio_link,
                cover_image=wagtail_image,
            )
            parent_page.add_child(instance=episode_page)
            self.stdout.write(f"Episode '{title}' added successfully.")

        self.stdout.write("Update completed.")
        
