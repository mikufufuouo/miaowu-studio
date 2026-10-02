#!/usr/bin/env python3
"""Copy this static site and set its real public address. Standard library only."""

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
STUDIO = "喵呜小暖工作室"
DESCRIPTION = "喵呜小暖工作室是一间由兴趣驱动的独立游戏工作室，正在认真开发与运营《决战捞妹之巅：第五电竞经理》。"


def prepare(base_url, output):
    parsed = urlsplit(base_url)
    if (parsed.scheme not in ("https", "http") or not parsed.netloc
            or parsed.query or parsed.fragment or parsed.username or parsed.password):
        raise ValueError("--base-url must be a public http(s) site address without credentials, query or fragment")
    base = base_url.rstrip("/") + "/"
    destination = Path(output).resolve()
    if destination == ROOT or ROOT.is_relative_to(destination):
        raise ValueError("Output must not be the source directory or one of its parents")
    # Only remove files this script previously generated, never the whole output directory.
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "404.html", ".nojekyll"):
        shutil.copy2(ROOT / name, destination / name)
    shutil.copytree(ROOT / "assets", destination / "assets", dirs_exist_ok=True)

    homepage = (destination / "index.html").read_text(encoding="utf-8")
    # Absolute image URLs are required for previews on social platforms.
    for key, attribute in (("og:image", "property"), ("twitter:image", "name")):
        homepage = re.sub(
            r'(<meta\s+' + attribute + r'="' + re.escape(key) + r'"\s+content=")[^"]*(")',
            lambda match: match.group(1) + html.escape(base + "assets/og-image.png", quote=True) + match.group(2),
            homepage,
        )
    structured = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": STUDIO,
        "alternateName": "Miaowu Xiaonuan Studio",
        "description": DESCRIPTION,
        "url": base,
        "inLanguage": "zh-CN",
        "publisher": {
            "@type": "Organization",
            "name": STUDIO,
            "url": base,
            "logo": base + "assets/studio-logo.png",
            "sameAs": ["https://www.taptap.cn/developer/432179", "https://github.com/mikufufuouo"],
        },
    }
    escaped = html.escape(base, quote=True)
    extra = (
        f'  <link rel="canonical" href="{escaped}">\n'
        f'  <meta property="og:url" content="{escaped}">\n'
        f'  <meta property="og:site_name" content="{STUDIO}">\n'
        '  <meta property="og:locale" content="zh_CN">\n'
        '  <meta property="og:image:width" content="1200">\n'
        '  <meta property="og:image:height" content="630">\n'
        '  <meta property="og:image:type" content="image/png">\n'
        f'  <meta property="og:image:alt" content="{STUDIO}与作品《决战捞妹之巅》的品牌分享图">\n'
        '  <script type="application/ld+json">' + json.dumps(structured, ensure_ascii=False) + '</script>\n'
    )
    homepage = homepage.replace("</head>", extra + "</head>", 1)
    (destination / "index.html").write_text(homepage, encoding="utf-8")
    # A GitHub Pages 404 is served under the requested path, sometimes many folders deep.
    missing = (destination / "404.html").read_text(encoding="utf-8")
    missing = re.sub(r'((?:href|src)=")assets/', lambda match: match.group(1) + escaped + "assets/", missing)
    missing = missing.replace('href="./"', 'href="' + escaped + '"')
    missing = missing.replace("</head>", '  <meta name="robots" content="noindex">\n</head>', 1)
    (destination / "404.html").write_text(missing, encoding="utf-8")
    (destination / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: " + base + "sitemap.xml\n", encoding="utf-8")
    (destination / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url><loc>' + html.escape(base) + '</loc></url>\n'
        '</urlset>\n', encoding="utf-8")
    print(f"Prepared {destination} for {base}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True, help="Actual Pages URL or custom domain")
    parser.add_argument("--output", default=str(ROOT / "_site"))
    arguments = parser.parse_args()
    prepare(arguments.base_url, arguments.output)
