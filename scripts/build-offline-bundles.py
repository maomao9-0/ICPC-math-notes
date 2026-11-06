#!/usr/bin/env python3
"""
Post-render script to build standalone offline HTML .zip bundles for each textbook
(and a combined all-books bundle) in `_site/downloads/`.

Each archive includes:
- The rendered HTML pages of the selected textbook (`fps/`, `flows/`, or `math/`)
- Local KaTeX math rendering (`assets/katex/`) replacing the external MathJax CDN
- Shared `site_libs/` and `assets/` with external Google Fonts `@import` stripped
  so pages render immediately without internet access
- Offline `file://`-compatible full-text search (`search-index.js` + `search.json`)
  filtered to the selected textbook
- A top-level `index.html` entry point and `README.md` for immediate local browsing
"""

from __future__ import annotations

import json
import os
import re
import shutil
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT_DIR / "_site"
KATEX_SRC_DIR = ROOT_DIR / "assets" / "katex"
DOWNLOADS_DIR = SITE_DIR / "downloads"

BOOKS = {
    "fps": {
        "zip_name": "icpc-fps-offline.zip",
        "folder_name": "icpc-fps-offline",
        "title": "Textbook I · Formal Power Series & Generating Functions (Ch 01–24)",
        "short_title": "Formal Power Series & Generating Functions",
        "entry": "fps/index.html",
        "dirs": ["fps"],
    },
    "flows": {
        "zip_name": "icpc-flows-offline.zip",
        "folder_name": "icpc-flows-offline",
        "title": "Textbook II · Network Flows, Minimum Cuts, Matching, Duality & Modelling (Ch 01–24)",
        "short_title": "Network Flows & Modelling",
        "entry": "flows/index.html",
        "dirs": ["flows"],
    },
    "math": {
        "zip_name": "icpc-math-offline.zip",
        "folder_name": "icpc-math-offline",
        "title": "Textbook III · Competitive Programming Mathematics (00–20)",
        "short_title": "Competitive Programming Mathematics",
        "entry": "math/index.html",
        "dirs": ["math"],
    },
    "all": {
        "zip_name": "icpc-all-books-offline.zip",
        "folder_name": "icpc-all-books-offline",
        "title": "ICPC Math Notes · All Three Textbooks Combined (FPS, Network Flows & CP Mathematics)",
        "short_title": "All Three Textbooks",
        "entry": "index.html",
        "dirs": ["fps", "flows", "math"],
    },
}

OFFSET_RE = re.compile(r'<meta\s+name="quarto:offset"\s+content="([^"]*)"\s*/?>')

CDN_MATHJAX_RE = re.compile(
    r'\s*<script src="https://cdnjs\.cloudflare\.com/polyfill/v3/polyfill\.min\.js\?features=es6"></script>\s*'
    r'<script defer="" src="https://cdn\.jsdelivr\.net/npm/mathjax@[^"]+" type="text/javascript"></script>',
    re.MULTILINE,
)

TYPESET_MATH_RE = re.compile(
    r"<script type=\"text/javascript\">\s*const typesetMath = \(el\) => \{.*?\};?\s*window\.Quarto = \{\s*typesetMath\s*\};\s*</script>",
    re.DOTALL,
)

GOOGLE_FONTS_IMPORT_RE = re.compile(
    r'@import\s+url\(["\']https://fonts\.googleapis\.com/[^"\']+["\']\);?'
)

OFFLINE_DROPDOWN_RE = re.compile(
    r'\s*<ul class="navbar-nav navbar-nav-scroll ms-auto">\s*<li class="nav-item dropdown ">.*?</ul>\s*</li>\s*</ul>',
    re.DOTALL,
)

SEARCH_FILE_ALERT_TARGET = """    if (window.location.protocol === "file:" && !shownWarning) {
      window.alert(
        "Search requires JavaScript features disabled when running in file://... URLs. In order to use search, please run this document in a web server."
      );
      shownWarning = true;
      return;
    }
    const fuse = new window.Fuse([], kFuseIndexOptions);"""

SEARCH_FILE_OFFLINE_REPLACEMENT = """    const fuse = new window.Fuse([], kFuseIndexOptions);
    if (window.location.protocol === "file:") {
      if (!window.__OFFLINE_SEARCH_DOCS__) {
        await new Promise((resolve, reject) => {
          const s = document.createElement("script");
          s.src = offsetURL("search-index.js");
          s.onload = resolve;
          s.onerror = reject;
          document.head.appendChild(s);
        });
      }
      (window.__OFFLINE_SEARCH_DOCS__ || []).forEach(function (searchDoc) {
        fuse.add(searchDoc);
      });
      fuseIndex = fuse;
      return fuseIndex;
    }"""


def make_offline_typeset_script() -> str:
    return """<script type="text/javascript">
const stripMathDelimiters = (tex) => {
  const t = tex.trim();
  if ((t.startsWith("\\\\(") && t.endsWith("\\\\)")) || (t.startsWith("\\\\[") && t.endsWith("\\\\]"))) {
    return t.slice(2, -2);
  }
  return tex;
};
const typesetMath = (el) => {
  if (window.katex) {
    var mathElements = el.getElementsByClassName("math");
    var macros = {};
    for (var i = 0; i < mathElements.length; i++) {
      var item = mathElements[i];
      if (item.tagName === "SPAN" && item.getAttribute("data-katex-rendered") !== "1") {
        var rawTex = item.getAttribute("data-raw-tex") || item.textContent || "";
        item.setAttribute("data-raw-tex", rawTex);
        window.katex.render(stripMathDelimiters(rawTex), item, {
          displayMode: item.classList.contains("display"),
          throwOnError: false,
          strict: false,
          macros: macros,
          fleqn: false
        });
        item.setAttribute("data-katex-rendered", "1");
      }
    }
  } else if (window.MathJax) {
    window.MathJax.typeset([el]);
  }
};
window.Quarto = {
  typesetMath
};
document.addEventListener("DOMContentLoaded", function () {
  typesetMath(document.body);
});
</script>"""


def transform_html_for_offline(html_text: str) -> str:
    m = OFFSET_RE.search(html_text)
    offset = m.group(1) if m else "./"

    katex_tags = (
        f'\n  <link rel="stylesheet" href="{offset}assets/katex/katex.min.css">'
        f'\n  <script defer src="{offset}assets/katex/katex.min.js"></script>'
    )
    if CDN_MATHJAX_RE.search(html_text):
        html_text = CDN_MATHJAX_RE.sub(lambda _: katex_tags, html_text)
    elif "assets/katex/katex.min.js" not in html_text:
        html_text = html_text.replace("</head>", f"{katex_tags}\n</head>", 1)

    offline_typeset = make_offline_typeset_script()
    if TYPESET_MATH_RE.search(html_text):
        html_text = TYPESET_MATH_RE.sub(lambda _: offline_typeset, html_text)

    html_text = html_text.replace(
        '<script src="/assets/accessibility.js" defer></script>',
        f'<script src="{offset}assets/accessibility.js" defer></script>',
    )
    html_text = OFFLINE_DROPDOWN_RE.sub("", html_text)
    return html_text


def make_root_redirect_html(title: str, target_href: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Offline Edition</title>
  <meta http-equiv="refresh" content="0; url={target_href}">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <style>
    body {{
      font-family: system-ui, -apple-system, sans-serif;
      max-width: 42rem;
      margin: 4rem auto;
      padding: 0 1.25rem;
      line-height: 1.6;
      color: #1f2328;
    }}
    a {{ color: #0969da; }}
  </style>
  <script>window.location.replace("{target_href}");</script>
</head>
<body>
  <h1>{title}</h1>
  <p>Opening the offline textbook… If you are not redirected automatically, <a href="{target_href}">click here to open {title}</a>.</p>
</body>
</html>
"""


def make_other_book_stub_html(included_title: str, included_entry: str, missing_title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Not Included in This Single-Book Offline Bundle</title>
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
  <style>
    body {{
      font-family: system-ui, -apple-system, sans-serif;
      max-width: 42rem;
      margin: 4rem auto;
      padding: 0 1.25rem;
      line-height: 1.65;
      color: #1f2328;
    }}
    .box {{
      border: 1px solid #d8dee4;
      background: #f6f8fa;
      padding: 1.25rem 1.5rem;
      border-radius: 0.25rem;
    }}
    a {{ color: #0969da; font-weight: 500; }}
  </style>
</head>
<body>
  <div class="box">
    <h1 style="margin-top: 0; font-size: 1.35rem;">Single-Book Offline Archive</h1>
    <p>This offline archive contains <strong>{included_title}</strong> only, so <em>{missing_title}</em> is not bundled in this download.</p>
    <p><a href="../{included_entry}">← Return to {included_title}</a></p>
  </div>
</body>
</html>
"""


def make_readme(title: str, entry: str) -> str:
    return f"""# {title} (Offline HTML Edition)

## How to Read Offline

1. Unzip this archive to any folder on your computer or tablet.
2. Open `index.html` (or `{entry}`) in any modern web browser (Chrome, Firefox, Safari, or Edge).

## Offline Features Included

- **100% Offline Math Rendering**: Bundled with local KaTeX scripts and WOFF2 fonts (`assets/katex/`), so no internet connection is required to render formulas.
- **Interactive Navigation & Callouts**: Full docked chapter sidebar, table of contents, light/dark mode toggle, and collapsible solution callouts.
- **Offline Full-Text Search**: Press `/` or `f` (or click the search icon in the top navigation bar) to search chapters offline, even when browsing directly via `file://` URLs without a local web server.
"""


def ensure_katex_in_site() -> None:
    dst = SITE_DIR / "assets" / "katex"
    if KATEX_SRC_DIR.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(KATEX_SRC_DIR, dst)


def collect_common_files() -> dict[str, bytes]:
    """Read shared `assets/` and `site_libs/` once and prepare their offline bytes."""
    common: dict[str, bytes] = {}

    for sub in ("assets", "site_libs"):
        base = SITE_DIR / sub
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(SITE_DIR).as_posix()
            data = path.read_bytes()
            if rel.startswith("site_libs/bootstrap/") and rel.endswith(".css"):
                text = data.decode("utf-8", errors="ignore")
                text = GOOGLE_FONTS_IMPORT_RE.sub("", text)
                data = text.encode("utf-8")
            elif rel == "site_libs/quarto-search/quarto-search.js":
                text = data.decode("utf-8", errors="ignore")
                if SEARCH_FILE_ALERT_TARGET in text:
                    text = text.replace(SEARCH_FILE_ALERT_TARGET, SEARCH_FILE_OFFLINE_REPLACEMENT, 1)
                data = text.encode("utf-8")
            common[rel] = data

    return common


def build_bundle(
    key: str,
    spec: dict,
    common_files: dict[str, bytes],
    all_search_docs: list[dict],
) -> Path:
    folder = spec["folder_name"]
    zip_path = DOWNLOADS_DIR / spec["zip_name"]
    included_dirs: list[str] = spec["dirs"]

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        # 1. Shared assets and site_libs
        for rel, content in common_files.items():
            zf.writestr(f"{folder}/{rel}", content)

        # 2. README.md
        zf.writestr(
            f"{folder}/README.md",
            make_readme(spec["title"], spec["entry"]).encode("utf-8"),
        )

        # 3. Root index.html (either full portal for 'all' or immediate redirect for single book)
        if key == "all":
            root_index = SITE_DIR / "index.html"
            if root_index.is_file():
                html_str = root_index.read_text(encoding="utf-8")
                zf.writestr(
                    f"{folder}/index.html",
                    transform_html_for_offline(html_str).encode("utf-8"),
                )
        else:
            zf.writestr(
                f"{folder}/index.html",
                make_root_redirect_html(spec["title"], spec["entry"]).encode("utf-8"),
            )
            # Also add friendly stubs for the other two books so navbar links never 404
            for other_key in ("fps", "flows", "math"):
                if other_key not in included_dirs:
                    other_title = BOOKS[other_key]["title"]
                    stub_html = make_other_book_stub_html(
                        spec["title"], spec["entry"], other_title
                    )
                    zf.writestr(f"{folder}/{other_key}/index.html", stub_html.encode("utf-8"))

        # 4. Book directory contents
        for book_dir in included_dirs:
            src_book = SITE_DIR / book_dir
            if not src_book.is_dir():
                continue
            for path in src_book.rglob("*"):
                if not path.is_file():
                    continue
                rel = path.relative_to(SITE_DIR).as_posix()
                if path.suffix.lower() == ".html":
                    html_str = path.read_text(encoding="utf-8")
                    data = transform_html_for_offline(html_str).encode("utf-8")
                else:
                    data = path.read_bytes()
                zf.writestr(f"{folder}/{rel}", data)

        # 5. Filtered search.json and search-index.js (for file:// offline search)
        if key == "all":
            filtered_docs = all_search_docs
        else:
            prefixes = tuple(f"{d}/" for d in included_dirs)
            filtered_docs = [
                doc
                for doc in all_search_docs
                if str(doc.get("href", "")).startswith(prefixes)
                or str(doc.get("objectID", "")).startswith(prefixes)
            ]

        search_json_str = json.dumps(filtered_docs, ensure_ascii=False)
        zf.writestr(f"{folder}/search.json", search_json_str.encode("utf-8"))
        zf.writestr(
            f"{folder}/search-index.js",
            f"window.__OFFLINE_SEARCH_DOCS__ = {search_json_str};\n".encode("utf-8"),
        )

    return zip_path


def main() -> None:
    if not SITE_DIR.is_dir():
        return

    # Only build bundles if all three book directories exist in _site
    if not all((SITE_DIR / d).is_dir() for d in ("fps", "flows", "math")):
        return

    ensure_katex_in_site()
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    common_files = collect_common_files()

    search_json_path = SITE_DIR / "search.json"
    all_search_docs: list[dict] = []
    if search_json_path.is_file():
        try:
            all_search_docs = json.loads(search_json_path.read_text(encoding="utf-8"))
        except Exception:
            all_search_docs = []

    for key, spec in BOOKS.items():
        zip_path = build_bundle(key, spec, common_files, all_search_docs)
        size_mb = zip_path.stat().st_size / (1024 * 1024)
        print(f"[offline-bundles] Built {zip_path.relative_to(ROOT_DIR)} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
