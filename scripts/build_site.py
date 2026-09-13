"""Export an allowlisted static site. Never package private worker files."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    source, target = ROOT / 'site', ROOT / 'dist'
    feed = json.loads((source / 'data/feed.json').read_text())
    if feed.get('demo'):
        raise ValueError('Refusing to publish illustrative data')
    if target.exists():
        shutil.rmtree(target)
    for name in ('index.html','app.js','styles.css','favicon.svg','robots.txt','data/feed.json'):
        destination = target / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / name, destination)
    (target / '.nojekyll').touch()
    print('Static site built in dist/ (public files only).')


if __name__ == '__main__':
    build()

