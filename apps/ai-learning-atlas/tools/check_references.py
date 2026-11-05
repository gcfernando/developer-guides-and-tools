"""Explicit online authoring check; the reader never calls this script."""
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()

    def handle_starttag(self, tag, attributes):
        values = dict(attributes)
        if tag == 'a' and values.get('href', '').startswith(('https://', 'http://')):
            self.urls.add(values['href'])


def check(url):
    try:
        request = Request(url, headers={'User-Agent': 'Atlas-reference-verification/1.0'})
        with urlopen(request, timeout=25) as response:
            response.read(1024)
            return {'url': url, 'status': response.status, 'final_url': response.url,
                    'result': 'resolved'}
    except HTTPError as error:
        return {'url': url, 'status': error.code, 'final_url': error.url,
                'result': 'unverified' if error.code in (401, 403, 429) else 'failed',
                'error': str(error)}
    except (URLError, TimeoutError, OSError) as error:
        return {'url': url, 'result': 'unverified', 'error': str(error)}


if __name__ == '__main__':
    from check_atlas import Document
    document = Document((ROOT/'index.html').read_text(encoding='utf-8'))
    links = Links()
    links.urls = {n.attrs['href'] for n in document.nodes if n.tag == 'a' and n.attrs.get('href', '').startswith(('http://', 'https://'))}
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(check, sorted(links.urls)))
    report = {'checked_on': date.today().isoformat(), 'method': 'GET with redirects, first 1024 bytes; reachability does not verify every statement', 'links': results}
    output = ROOT.parents[1]/'artifacts/ai-learning-atlas/reference-checks.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    for result in results:
        print(result['result'].upper(), result.get('status', ''), result['url'], '=>', result.get('final_url', result.get('error', '')))
    print('Resolved', sum(r['result'] == 'resolved' for r in results), 'of', len(results))
