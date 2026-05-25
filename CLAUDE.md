# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal website for Jonathan Mikler (Robotics Engineer, M.Sc. Autonomous Systems, DTU). The site is content-first: Markdown files and HTML pages served as-is — likely via GitHub Pages or a similar static host. There is no build system, bundler, or framework.

## Repository structure

- `index.md` — Main landing page: bio, professional highlights, academics, and blog posts index
- `articles/` — Long-form blog content. Markdown (`.md`) for drafts/prose; exported Notion HTML (`.html`) for published articles
- `courses/` — PDF course materials and posters, organized per course
- `media/` — Images referenced by `index.md` and articles
- `drafts/` — Pending ideas (`pending.md`)

## Content conventions

### Adding a blog post
1. Write the article as Markdown or export it from Notion as HTML and place it under `articles/<topic>/`.
2. Add a link to it in the `# Blog Posts` section of `index.md`.

### HTML articles (Notion exports)
The thesis article (`articles/thesis/ee-in-cv-pt1.html`) is a full self-contained Notion export with inlined CSS. `articles/thesis/split.py` is a utility to split that large file into per-`<h1>` section files — run it from inside `articles/thesis/`:

```bash
cd articles/thesis && python3 split.py
```

Output goes to `articles/thesis/article_sections/`.

### Markdown articles with images
Images should sit next to the `.md` file and be referenced with relative paths (e.g. `![alt](urnChoice1.png)`). For inline HTML image blocks, use the centered `<div>` pattern already used in `articles/bayesian/midSummer_Bayesian.md`.

## Linking conventions in index.md

- Internal files: relative paths (e.g. `courses/thesis/Study_of_...pdf`)
- External: full URLs (GitHub, LinkedIn, Google Drive, DTU course pages)
- The CV links to a Google Drive folder, not a file — keep it that way for easy updates without changing `index.md`
