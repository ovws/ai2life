# AI2Life

文章发布项目，使用 GitHub Pages 公开托管。首页为文章列表，每篇文章以宋体排版、全文展示。

- 项目：https://github.com/ovws/ai2life
- 网站：https://ovws.github.io/ai2life/
- 第一篇：https://ovws.github.io/ai2life/articles/choices/

## 发布文章

1. 将文章的完整 HTML 保存为 `articles/<slug>/index.html`。
2. 在 `articles.json` 添加 `slug`、`title`、`date`、`summary`。
3. 执行 `python scripts/build.py` 更新首页。
4. 提交到 `main`；GitHub Pages 自动发布。

后续可以直接告诉助手：“发布到 ovws/ai2life，后缀用 <slug>”，并提供文章。未指定后缀时，使用简短、唯一的小写英文后缀；不要覆盖已有文章。

## 自定义域名

目前尚未绑定自定义域名。提供完整域名后，在 GitHub Pages 中配置域名及对应 DNS；DNS 就绪后启用 HTTPS。不要将 ChatGPT Site 域名当作可自行管理的域名。

文章地址会从 `https://ovws.github.io/ai2life/articles/<slug>/` 变为 `https://你的域名/articles/<slug>/`，无需修改文章目录或首页的相对链接。新绑定域名前保留现有配置，并先确认 DNS 管理权限。

## 验证

`python scripts/build.py` 会检查后缀格式、重复后缀和文章页面是否存在。
