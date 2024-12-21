import csv
import requests
from io import BytesIO
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from wagtail.images.models import Image
from podcast.models import EpisodePage, EpisodeIndexPage
from wagtail.models import Page
from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_time_string(time_str):
    parts = time_str.split(':')
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
    elif len(parts) == 2:
        hours, minutes, seconds = 0, *map(int, parts)
    else:
        raise ValueError("Invalid time format")
    
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)


class Command(BaseCommand):
    help = 'Import episodes from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Parent page where episodes will be added
        parent_page = EpisodeIndexPage.objects.first()

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                duration = convert_time_string(row['Duration'])

                upload_date = row['Date Complex']
                upload_date = datetime.strptime(upload_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()

                image_url = row['Cover URL']
                image_title = row['Title']

                response = requests.get(image_url)
                if response.status_code == 200:
                    image_data = BytesIO(response.content)
                    wagtail_image = Image(title=image_title)
                    wagtail_image.file = InMemoryUploadedFile(image_data, None, image_title + '.jpg', 'image/jpeg', len(response.content), None)
                    wagtail_image.save()

                episode_page = EpisodePage(
                    title=row['Title'],
                    date=upload_date,
                    intro=row['Intro'],
                    body=row['Notes'],
                    duration=duration,
                    authors_old=row['People'],
                    sound_cloud_url=row['Page URL'],
                    cover_image=wagtail_image,
                )
                parent_page.add_child(instance=episode_page)
                self.stdout.write(f"Added episode: {row['Title']}")

        self.stdout.write("Import completed.")
