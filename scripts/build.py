from pathlib import Path
from html import escape
import json,re
root=Path(__file__).resolve().parents[1]
articles=json.loads((root/'articles.json').read_text())
seen=set()
for a in articles:
 s=a['slug']
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',s) or s in seen:raise ValueError('Invalid or duplicate article slug: '+s)
 seen.add(s)
 if not (root/'articles'/s/'index.html').is_file():raise ValueError('Missing article: '+s)
items=''.join('<li><time>'+escape(a['date'])+'</time><h2><a href="articles/'+a['slug']+'/">'+escape(a['title'])+'</a></h2><p>'+escape(a.get('summary',''))+'</p></li>' for a in sorted(articles,key=lambda a:a['date'],reverse=True))
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI2Life · 文章</title><meta name="description" content="关于 AI、生活与人的选择。"><style>*{box-sizing:border-box}body{margin:0;color:#171717;background:#fff;font-family:"Songti SC","STSong","SimSun","Noto Serif CJK SC",serif;font-size:18px;line-height:1.9}main{max-width:760px;margin:auto;padding:40px 24px}h1{font-size:30px;font-weight:400;margin:0 0 32px}ul{padding:0;list-style:none}li{padding:24px 0;border-top:1px solid #ddd}h2{font-size:23px;font-weight:400;line-height:1.6;margin:8px 0}time{font-size:14px;color:#666}p{margin:8px 0;color:#555}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:2px solid #555;outline-offset:4px}</style></head><body><main><h1>AI2Life</h1><ul>'''+items+'</ul></main></body></html>'
(root/'index.html').write_text(page)
print('Generated homepage:',len(articles),'articles')
