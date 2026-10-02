# 喵呜小暖工作室官网

一个长期维护的静态单页官网：原生 HTML + CSS、本地图片，没有框架、网站运行时 JavaScript、数据库、CDN 字体或分析服务。页面直接打开即可阅读；GitHub Pages 发布时由一个 Python 标准库脚本补齐实际网址和搜索信息。

## 本地查看

在这个目录执行：

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

打开 `http://127.0.0.1:4173`。也可以直接在浏览器打开 `index.html`。

## 日常更新

- `index.html`：工作室文案、游戏资料、状态和外部入口。`#about` 是简介，`#games` 是作品，`#values` 是理念。
- `assets/site.css`：分区注释的样式。顶部 `:root` 是品牌配色；窄屏规则位于下方。
- `assets/`：所有图片、分享图和图标。原工作室及游戏 PNG Logo 保留；网页使用更小的 WebP 派生文件。
- `ASSETS.md`：图片来源与处理记录。
- `design/og-card.html`：1200 × 630 分享图的布局源文件。调整后以该视口尺寸导出 PNG，保存为 `assets/og-image.png`。
- `scripts/prepare_pages.py`：仅负责发布文件和网址处理，不参与访客浏览。

新增真实游戏时，复制 `#games` 里的一个 `<article class="game-card">`，替换图片、标题、简介、状态、链接和作品编号，再同步调整标题旁的作品数量。每张卡片会自动留出间距；不需要改后端或组件系统。

外部入口已确认：

- 工作室 TapTap：<https://www.taptap.cn/developer/432179>
- 游戏 TapTap：<https://www.taptap.cn/app/902608>
- GitHub：<https://github.com/mikufufuouo>

## GitHub Pages 发布

站点文件和 `.github/workflows/pages.yml` 已准备好。远程仓库由你选择；建议使用公开仓库 `mikufufuouo/miaowu-studio`，默认分支为 `main`。

1. 将本目录的 Git 仓库上传到 GitHub，包含 `.github/workflows/pages.yml`。
2. 在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
3. 在 **Actions → Publish studio website → Run workflow** 运行首次发布。之后推送到 `main` 会自动发布。

工作流使用 GitHub 官方 Pages Actions，自动读取实际 Pages 地址，生成正确的 canonical、Open Graph 绝对链接、JSON-LD、`robots.txt` 和 `sitemap.xml`。适配根站点、项目子路径和已配置的自定义域名；无需手改站点域名。404 的资源与回首页链接也会转成实际官网绝对地址。

发布产物仅包含网页、`assets/`、`.nojekyll` 和搜索文件；文档、设计源文件、浏览器检查截图与脚本不会被发布。网站不需要设置额外 Token 或服务密钥。

若要生成可交给其他静态托管服务的产物：

```sh
python3 scripts/prepare_pages.py --base-url 'https://你的实际官网地址/'
```

生成内容位于 `_site/`。这里填写实际域名，原始文件无需更改。

## 品牌边界

猫咪是工作室的原有吉祥物；奶油白、暖灰棕和少量肉垫粉延伸个人气质。作品区保留游戏自身的电竞视觉，主视觉不加猫。文案与作品只使用真实信息；只保留已确认的外部账号。

细节限于按钮轻微按压、理念卡片轻抬、一个小猫爪装饰和原猫脸派生图标。支持键盘焦点、跳过导航和系统减少动态效果偏好。
