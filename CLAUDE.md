# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website for stevenkasapi.net, built with [Pelican](https://getpelican.com/) (Python static site generator).

## Commands

Activate the venv first:

```bash
source .venv/bin/activate
```

The venv was created with Python 3.12 (`python3.12 -m venv .venv`). The system default `python3` is 3.8 and is too old for current Pelican.

```bash
# Local development build
pelican content

# Serve locally with auto-reload
pelican --listen

# Production build — SITEURL defaults to stevenkasapi.net if not set
PYTHONPATH=. pelican content -s publishconf.py

# Production build targeting a different host
SITEURL="https://other-host.com" PYTHONPATH=. pelican content -s publishconf.py

# Deploy to FTP host (stevenkasapi.net)
./deploy.sh
```

## Architecture

```
pelicanconf.py      # Dev config (SITEURL="", feeds disabled, RELATIVE_URLS=True)
publishconf.py      # Production overrides (imports pelicanconf.py, sets live URL)
content/
  pages/            # Static pages: photography.md, professional.md, contact.md
  posts/            # Blog articles, organised as {year}/{YYYY-mm-dd-slug}.md
  images/           # banner.jpg, photography_banner.jpg, professional_banner.jpg
  extra/            # Files copied verbatim to output root (e.g. CNAME, robots.txt)
themes/kasapi/
  templates/        # Jinja2 templates (base.html, home.html, index.html, page.html, article.html, archives.html)
  static/css/       # style.css — single stylesheet using CSS custom properties
output/             # Generated site — not committed; deploy this directory
.github/workflows/  # GitHub Actions — deploys to GitHub Pages on push to main
deploy.sh           # FTP deploy script for stevenkasapi.net
```

## Theme

The custom `kasapi` theme is a minimal, content-first design. Key design tokens are CSS variables defined at `:root` in `style.css` (colors, font stack, `--measure` line length, spacing scale). All templates extend `base.html`.

- Homepage uses `TEMPLATE_PAGES` to render `home.html` → `index.html`
- Blog index is at `/blog/` via `INDEX_SAVE_AS`
- Blog link is hardcoded in `base.html` and `home.html` using `{{ SITEURL }}/blog/` to stay relative with `RELATIVE_URLS = True`

## Content

Pages use Pelican's standard Markdown front matter:
```markdown
Title: Page Title
Slug: url-slug
Status: published
```

Per-page banners set via `Banner:` front matter metadata; fallback to `banner.jpg` in `base.html`.

URLs: pages at `/{slug}/`, posts at `/posts/{slug}/`.

Tag, category, author, and per-author archive pages are disabled (`*_SAVE_AS = ""`).

## Configuration Notes

- `pelicanconf.py` is the single source of truth; `publishconf.py` only overrides what differs in production.
- `SITEINTRO` in `pelicanconf.py` accepts HTML and controls the homepage blurb.
- The site must remain portable across hosts. `SITEURL` in `publishconf.py` reads from the `SITEURL` environment variable. Never hardcode a hostname in templates or config.
