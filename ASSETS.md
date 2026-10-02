# 图片来源

- `assets/studio-logo.png`：复制自用户提供的 `/Users/mikufufu/Desktop/工作室logo_512x512.png`。保留原有猫咪与中英文标志，用于导航、Hero 吉祥物与页脚。
- `assets/favicon-32.png`、`assets/favicon.png`（64px）、`assets/apple-touch-icon.png`（180px）：从工作室原 logo 裁取猫脸区域，用作网站和主屏幕图标；完整 Logo 原图仍保存在 `assets/studio-logo.png`。
- `assets/game-key-art.jpg`：压缩自用户提供的 `/Users/mikufufu/Desktop/主页重构_生图资产_20260923/bg_arena_source.png`，作为电竞舞台背景。
- `assets/game-logo.png`：从用户提供的 `/Users/mikufufu/Desktop/主页重构_生图资产_20260923/logo_dwrg_full_source.png` 等比缩至宽 1000px、保留透明度，叠加展示游戏原标志。

品牌图形未重绘。网站使用的游戏资料链接为 TapTap 官方游戏页：https://www.taptap.cn/app/902608

## 轻量资源与分享图

- `assets/studio-logo.webp`：由上述原工作室 PNG 在本地转码，512 × 512，网页显示用；原 PNG 保留。
- `assets/game-logo.webp`：由上述透明游戏 PNG Logo 在本地转码，1000 × 333，保留透明背景和游戏原有字形。
- `assets/og-image.png`：1200 × 630 本地品牌分享图，用 `design/og-card.html` 排版并在浏览器导出；组成元素仍是原工作室 Logo、原游戏 Logo 和真实名称，没有重画角色。

网页没有外部图片请求。压缩与转码只用于尺寸/编码处理，不重新设计品牌。
