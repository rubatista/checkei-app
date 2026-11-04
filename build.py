"""Gera index.html (app instalável) a partir de src/app.html."""
from pathlib import Path
src = Path("src/app.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Checkei">
<meta name="theme-color" content="#F2F3F6">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-512.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""
# move <title>/meta/link/style into head, rest into body
idx = src.index("</style>") + len("</style>")
out = head + src[:idx] + "\n</head>\n<body>\n" + src[idx:] + "\n</body>\n</html>\n"
Path("index.html").write_text(out, encoding="utf-8")
print("index.html gerado")
