# Production settings
# Run: SITEURL="https://example.com" PYTHONPATH=. pelican content -s publishconf.py

import os
from pelicanconf import *

SITEURL = os.environ.get("SITEURL", "https://stevenkasapi.net")
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
