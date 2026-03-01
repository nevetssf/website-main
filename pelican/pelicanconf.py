import datetime

# --- Site identity --------------------------------------------------

AUTHOR = "Steven Kasapi"
SITENAME = "Steven Kasapi"
SITEDESCRIPTION = "Steven Kasapi's place on the web."
SITEURL = ""  # Leave empty for local dev; set to "https://stevenkasapi.net" for production
COPYRIGHT_YEAR = datetime.date.today().year

# --- Intro text shown on the home page -----------------------------
# HTML is fine here; keep it brief.

SITEINTRO = """
<p>Welcome to my public internet face.</p>
<p>Because this site is public, there aren't many personal details here.
If you know me, poke around and catch up on what I've been doing.
If you don't, it'll be a thin read — but you're welcome to look.</p>
"""

# --- Navigation ----------------------------------------------------
# Items that appear in the nav and on the home page, in addition to
# the auto-generated pages (Photography, Professional, Contact).
# "Public Journal" links to the WordPress blog.

MENUITEMS = [
    ("Public Journal", "https://stevenkasapi.net/blog/"),
]

# --- Paths ---------------------------------------------------------

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["posts"]
STATIC_PATHS = ["images", "extra"]

OUTPUT_PATH = "output/"

# --- URLs ----------------------------------------------------------

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
INDEX_SAVE_AS = "index.html"

# --- Theme ---------------------------------------------------------

THEME = "themes/kasapi"

# --- Feed generation -----------------------------------------------
# Disable feeds for local dev; enable for production.

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Misc ----------------------------------------------------------

TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 10

# Don't generate tag/category/author pages for a simple personal site
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = "archives/index.html"

RELATIVE_URLS = True
