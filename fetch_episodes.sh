#!/bin/bash

cd /srv/ || { echo "Failed to navigate to /srv/"; exit 1; }

source myenv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

cd filmbaratok/ || { echo "Failed to navigate to filmbaratok directory"; exit 1; }

python manage.py fetch_episodes || { echo "fetch_episodes failed"; exit 1; }

echo -e "\nLatest episodes have been fetched."