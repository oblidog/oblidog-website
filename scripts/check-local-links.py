"""Validate local HTML references without depending on external services."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src", "poster"):
            if key in attrs:
                self.refs.append(attrs[key])
        if "srcset" in attrs:
            self.refs.extend(item.strip().split()[0] for item in attrs["srcset"].split(",") if item.strip())


pages = {path: Page(path) for path in ROOT.glob("*.html")}
errors = []
for page, parsed in list(pages.items()):
    for ref in parsed.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        path = unquote(url.path)
        target = ((ROOT / path.lstrip("/")) if path.startswith("/") else (page.parent / path)).resolve() if path else page
        if not target.is_relative_to(ROOT):
            errors.append(f"{page.name}: reference escapes site root: {ref}")
            continue
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{page.name}: missing local file: {ref}")
        elif url.fragment and target.suffix == ".html":
            if target not in pages:
                pages[target] = Page(target)
            if unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{page.name}: missing anchor: {ref}")
if errors:
    raise SystemExit("\n".join(errors))
print("Local links, anchors and image sources are valid.")
