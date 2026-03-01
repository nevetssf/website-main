# Production settings — used when publishing to stevenkasapi.net
# Run: pelican content -s publishconf.py

from pelicanconf import *

SITEURL = "https://stevenkasapi.net"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
