"""Check all rendered content routes, local assets, fragments, and search coverage.

Run after quarto render. Uses only the Python standard library.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.math = 0
        self.headings = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag in ('a', 'link') and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('img', 'script', 'iframe') and attrs.get('src'):
            self.links.append(attrs['src'])
        if 'math' in attrs.get('class', '').split():
            self.math += 1
        if tag in ('h1', 'h2', 'h3'):
            self.headings += 1


def main():
    sources = sorted(ROOT.glob('*.qmd')) + sorted(ROOT.glob('[0-9]*/*.qmd'))
    pages = {}
    errors = []
    for source in sources:
        path = SITE / source.relative_to(ROOT).with_suffix('.html')
        if not path.exists():
            errors.append(f'Missing rendered page: {path}')
        else:
            pages[path.resolve()] = Page(path)
    checked = 0
    for path, page in list(pages.items()):
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = ((SITE / unquote(url.path).lstrip('/')) if url.path.startswith('/')
                      else (path.parent / unquote(url.path))) if url.path else path
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            checked += 1
            if not target.exists():
                errors.append(f'{path.relative_to(SITE)}: missing {href}')
            elif url.fragment and target.suffix == '.html':
                if target not in pages:
                    pages[target] = Page(target)
                if unquote(url.fragment) not in pages[target].ids:
                    errors.append(f'{path.relative_to(SITE)}: missing fragment {href}')
    search_path = SITE / 'search.json'
    if not search_path.exists():
        errors.append('Missing search.json')
    else:
        entries = json.loads(search_path.read_text())
        searchable = {urlsplit(x['href']).path for x in entries}
        for source in sources:
            route = str(source.relative_to(ROOT).with_suffix('.html'))
            if route not in searchable:
                errors.append(f'Absent from search: {route}')
    for error in errors:
        print('ERROR:', error)
    print(f'{len(sources)} content pages; {checked} local links/assets checked; '
          f'{sum(p.math for p in pages.values())} math spans; {len(errors)} errors')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
