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

## Editorial and validation workflow

Start from `CONTENT_AUDIT.md` and `CURRICULUM.md`. Each chapter teaches objects
before algorithms and supplies worked failures, solved exercises, and library
contracts. See `AGENTS.md` for the concise policy.

Run `python tests/audit_foundations_math.py`, `python tests/audit_middle_math.py`,
`python tests/audit_models_math.py`, and `python tests/audit_frontier_math.py`,
then `quarto render` and `python scripts/check_site.py`.
`python scripts/check_external.py` reports external HTTP reachability separately.
`VALIDATION_REPORT.md` records the latest findings and limitations.

For optional browser checks, install Playwright outside the source tree, install
its Chromium browser, serve `_site` on `127.0.0.1:8765`, and run
`node scripts/check_browser.cjs` with Playwright resolvable in `NODE_PATH`.
The checker visits every page at desktop and phone widths and writes sample
screenshots under `/tmp`. It is a development dependency, not a site runtime
dependency.

## Source structure

- `_quarto.yml` defines navigation, search, page navigation, and HTML options.
- `index.qmd` is the landing page.
- Numbered directories contain chapter and, where present, exercise pages.
- `assets/` contains the small visual theme. No generated site files belong in
  source control.

When adding a page, also add it to the sidebar in `_quarto.yml`. Link to source
pages by their `.qmd` paths; Quarto rewrites them to rendered HTML.
