# ICPC Math Notes website

This repository is a Quarto website containing a dependency-guided advanced
mathematics course for competitive programming.

## Preview locally

Install [Quarto](https://quarto.org/docs/get-started/), then run:

```sh
quarto preview
```

The development server reloads when a source file changes. To create the static
site without starting a server, run `quarto render`; output is written to
`_site/` and can be hosted by any static-site provider.

## Publish on GitHub Pages

The included workflow renders and publishes the site to a `gh-pages` branch on
each push to `main`. In the GitHub repository settings:

1. Under **Actions → General**, grant workflows read and write permission.
2. Under **Pages**, choose **Deploy from a branch**, then select `gh-pages` and
   the root directory.

After GitHub reports the public URL, add it as `website.site-url` in
`_quarto.yml` so canonical and social metadata use the final address.

## Structure

- `_quarto.yml` defines navigation, search, page navigation, and HTML options.
- `index.qmd` is the landing page.
- Numbered directories contain chapter and, where present, exercise pages.
- `assets/` contains the small visual theme. No generated site files belong in
  source control.

When adding a page, also add it to the sidebar in `_quarto.yml`. Link to source
pages by their `.qmd` paths; Quarto rewrites them to rendered HTML.
