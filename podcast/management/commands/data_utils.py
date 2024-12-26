import requests
from bs4 import BeautifulSoup
import json

def get_sound_data(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', text=lambda t: t and '__sc_hydration' in t)

    if script_tag:
        script_content = script_tag.string
        start_index = script_content.find('__sc_hydration = ') + len('__sc_hydration = ')
        end_index = script_content.find('};', start_index)  # Find the end of the JSON-like object
        hydration_data = json.loads(script_content[start_index:end_index])
        sound_data = next((item for item in hydration_data if item.get('hydratable') == 'sound'), None)
        if sound_data and 'data' in sound_data:
            description = sound_data['data'].get('description', '')
            publisher_metadata = sound_data['data'].get('publisher_metadata', {})
            artists = publisher_metadata.get('artist', '')

            return description, artists
        else:
            return None, None  # Return None if no sound data found
    else:
        return None, None  # Return None if no script tag found


import re

def replace_links_with_anchors(input_text):
    link_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    
    def link_replacement(match):
        url = match.group(0)
        href = url if url.startswith('http') else f'http://{url}'
        return f'<a href="{href}" target="_blank">{url}</a>'
    
    return re.sub(link_pattern, link_replacement, input_text)
