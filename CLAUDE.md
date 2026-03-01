# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal static website for stevenkasapi.net, built with [Pelican](https://getpelican.com/) (Python static site generator). All source files live under `pelican/`.

## Commands

All commands should be run from the `pelican/` directory. Activate the venv first:

```bash
source .venv/bin/activate
```

The venv was created with Python 3.12 (`python3.12 -m venv .venv`). The system default `python3` is 3.8 and is too old for current Pelican.

```bash
# Local development build
pelican content

# Serve locally with auto-reload
pelican --listen

# Production build (sets SITEURL, enables feeds, deletes output dir first)
pelican content -s publishconf.py
```

## Architecture

```
pelican/
  pelicanconf.py      # Dev config (SITEURL="", feeds disabled, RELATIVE_URLS=True)
  publishconf.py      # Production overrides (imports pelicanconf.py, sets live URL)
  content/
    pages/            # Static pages: photography.md, professional.md, contact.md
    posts/            # Blog articles (none yet)
    images/           # Images referenced in content
    extra/            # Files copied verbatim to output root (e.g. CNAME, robots.txt)
  themes/kasapi/
    templates/        # Jinja2 templates (base.html, index.html, page.html, article.html, archives.html)
    static/css/       # style.css — single stylesheet using CSS custom properties
  output/             # Generated site — not committed; deploy this directory
```

## Theme

The custom `kasapi` theme is a minimal, content-first design. Key design tokens are CSS variables defined at `:root` in `style.css` (colors, font stack, `--measure` line length, spacing scale). All templates extend `base.html`.

## Content

Pages use Pelican's standard Markdown front matter:
```markdown
Title: Page Title
Slug: url-slug
Status: published
```

URLs are configured as clean slugs: pages at `/{slug}/`, posts at `/posts/{slug}/`.

Tag, category, author, and per-author archive pages are disabled (`*_SAVE_AS = ""`).

## Configuration Notes

- `pelicanconf.py` is the single source of truth; `publishconf.py` only overrides what differs in production.
- `SITEINTRO` in `pelicanconf.py` accepts HTML and controls the homepage blurb.
- `MENUITEMS` adds external links (e.g. the WordPress blog) to the nav alongside auto-generated page links.
