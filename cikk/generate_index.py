import requests

sheet_id = "1js2SD4xPHS49y5Jo6pjBzScwXnePuTzE2yghCn2pJjU"
sheet_name = "Cikkek"

url = f"https://opensheet.elk.sh/{sheet_id}/{sheet_name}"

data = requests.get(url).json()

articles_html = ""

for article in data:

    title = article.get("cím") or article.get("Cím") or ""
    slug = article.get("slug") or ""
    excerpt = article.get("kivonat") or article.get("Kivonat") or ""

    if not title or not slug:
        continue

    articles_html += f"""
<div class="article">
<h2>{title}</h2>
<p>{excerpt}</p>
<a href="/cikk/{slug}.html">Elolvasom →</a>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<title>Cikkek – Ruhatárház</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta name="description" content="Hasznos cikkek használt ruhák vásárlásáról és öltözködésről.">

<style>

body{{
font-family:Inter, sans-serif;
background:#f6f6f6;
margin:0;
padding:40px 20px;
}}

.wrapper{{
max-width:900px;
margin:auto;
}}

h1{{
margin-bottom:30px;
}}

.article{{
background:white;
padding:22px;
border-radius:14px;
margin-bottom:20px;
border:1px solid #eee;
}}

.article h2{{
font-size:18px;
margin-bottom:6px;
}}

.article p{{
font-size:14px;
color:#666;
margin:0 0 10px 0;
}}

.article a{{
color:#3a7d2e;
text-decoration:none;
font-weight:600;
font-size:14px;
}}

.article a:hover{{
text-decoration:underline;
}}

</style>
</head>

<body>

<div class="wrapper">

<h1>Cikkek</h1>

{articles_html}

</div>

</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("index.html sikeresen generálva")
