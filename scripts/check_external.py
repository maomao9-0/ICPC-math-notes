"""Audit HTTP reachability separately from mathematical relevance.

Print JSON; do not alter chapter sources. Challenge pages are not accepted
as successful content verification. Invoke after all authors have saved sources.
"""
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path
import json
import re
import threading
import time
import urllib.error
import urllib.request
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
HOST_LOCKS = {}
HOST_LOCKS_LOCK = threading.Lock()


def check(url):
    host = urlsplit(url).netloc
    with HOST_LOCKS_LOCK:
        lock = HOST_LOCKS.setdefault(host, threading.Lock())
    with lock:
        result = fetch(url)
        # Respect host limits, particularly AtCoder's statement server.
        time.sleep(1 if host == 'atcoder.jp' else 0.15)
    return result


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'ICPC-math-notes-link-audit/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=18) as response:
            data = response.read(350000).decode('utf-8', errors='replace')
            match = re.search(r'<title[^>]*>(.*?)</title>', data, re.I | re.S)
            title = unescape(re.sub(r'\s+', ' ', match.group(1))).strip() if match else ''
            challenge = any(x in title.lower() for x in ('just a moment', 'attention required', 'access denied', 'ddos'))
            return {'url': url, 'status': 'challenge' if challenge else response.status,
                    'title': title, 'final_url': response.url}
    except urllib.error.HTTPError as e:
        return {'url': url, 'status': e.code, 'error': str(e)}
    except Exception as e:
        return {'url': url, 'status': 'unreachable', 'error': str(e)}


def main():
    urls = set()
    for path in sorted(ROOT.glob('*.qmd')) + sorted(ROOT.glob('[0-9]*/*.qmd')):
        urls.update(re.findall(r'https?://[^\s<>)"\]]+', path.read_text()))
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(check, sorted(urls)))
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
