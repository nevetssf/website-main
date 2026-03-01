#!/bin/bash
# Usage: ./deploy.sh
# Builds the site and uploads to stevenkasapi.net via FTP.

set -e

cd "$(dirname "$0")/pelican"

echo "Building site..."
SITEURL="https://stevenkasapi.net" PYTHONPATH=. .venv/bin/pelican content -s publishconf.py

echo "Uploading..."
lftp -e "
  set ftp:ssl-allow no;
  open -u stevenkasapi ftp.stevenkasapi.net;
  mirror --reverse --delete --verbose output/ public_html/;
  quit
"
