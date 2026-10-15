# Formatting validation — 2026-10-15

Scope: all 62 Quarto pages, including both the baseline and companion FPS tracks.

## Findings and repairs

- Markdown lists immediately following prose were parsed as paragraphs, exposing
  literal bullet and number markers. Added the missing block boundaries,
  including nested reasoning steps and lists following display mathematics.
- Raw HTML `details` elements containing Markdown headings interacted with
  Pandoc section divisions: the dropdown ended before its solution sections.
  Converted 257 such dropdowns to fenced Quarto callouts with `collapse="true"`.
  Outer fences are longer than any nested callout fences.
- Four numbered hint dropdowns in baseline chapter 08 escaped their containers.
  Converted them to fenced callouts, separated from the preceding list item text.
- Added the formatting convention to `AGENTS.md`. Expanded `check_site.py`
  from the baseline inventory to all 62 pages.

## Verification

- Full `quarto render`: passed without warnings or errors.
- `python3 scripts/check_site.py`: all 62 pages, local routes/assets,
  fragments, and search coverage: 9,019 local references checked, zero errors.
- `scripts/check_formatting.cjs`: checks every rendered page for empty or
  initially expanded dropdowns and exposed list/div/math delimiters; compares
  rendered dropdown counts with source counts (1,264 dropdowns). Exercises native hints and
  Quarto solution callouts at viewport widths 1440 and 390, confirming that
  solution headings become visible only when expanded and hide on closing.
- Source inspection confirmed balanced raw dropdown tags, no Markdown headings
  remaining inside raw dropdowns, and unchanged display formulas. A comparison
  ignoring whitespace and dropdown wrappers confirmed unchanged body content.
- `git diff --check`.

Browser check setup (Playwright and Chrome must already be installed):

```sh
python3 -m http.server 8765 --directory _site
# In another terminal; set NODE_PATH if Playwright is installed elsewhere:
BROWSER_EXECUTABLE=/usr/bin/google-chrome node scripts/check_formatting.cjs
```

Browser screenshots are written to `/tmp/icpc-format-solution-1440.png` and
`/tmp/icpc-format-solution-390.png`. Generated site output is not committed.
