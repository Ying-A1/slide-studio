# slide-studio

一个做「能改的」HTML 幻灯片的 coding-agent skill——用一个想法、一段笔记，或一个 PowerPoint 文件生成一套 slide，然后直接在浏览器里改文字、调排版、排顺序、加背景。

[English](README.md) ·  **中文**

<p>
  <a href="https://ying-a1.github.io/slide-studio/">打开在线演示</a> ·
  <a href="https://github.com/Ying-A1/slide-studio/releases">查看 Releases</a>
</p>

![slide-studio 演示](demo/cover.png)

打开演示后按 **E** 改文字、按 **O** 排序或复制页面、按 **G** 试用可选的图片面板。演示只使用 CSS 渐变，不需要 API Key。

## 这是什么

slide-studio 生成的是一个单文件、固定 16:9、零依赖的 `.html`。和「生成完就动不了」的工具不同，这个文件打开后自带编辑器：做好的 slide 还能接着改——重写文字、调字号行距、调整顺序、换背景，不用写代码，也不用再开别的软件。

## 主要功能

- **浏览器里改文字**——按 `E`，点任意文字直接输入。
- **排版控制**——选中文字弹出格式条，调字号、层级（大标题 / 标题 / 正文 / 小字）、行距、粗细、对齐。
- **幻灯片管理**——按 `O`，拖拽排序（或 ↑ ↓）、插入、复制、删除、点标题跳页；改完一键导出带着所有改动的干净 HTML。
- **可选 AI 背景**——按 `G`，用你自己的 OpenAI 兼容图像接口给某页生成电影感背景。纯可选，不填也能用渐变；仓库里不含任何密钥。
- **看着选风格**——从生成的首页预览里挑，背后是内置预设加 34 套 bold 模板，不用费劲描述审美。
- **PowerPoint 提取**——把 `.pptx` 的文字、图片、顺序和备注提取出来，作为制作网页 slide 的结构化起点。
- **导出 PDF / 在线链接**——导出 PDF，或部署成手机也能看的 Vercel 链接。
- **零依赖**——一个 HTML 文件，内联 CSS/JS，离线可用，任何屏幕都保持 16:9。
- **默认不「AI 味」**——内置一套设计规则，避开一眼假的套版。

## 安装

把 skill 克隆到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/Ying-A1/slide-studio.git ~/.claude/skills/slide-studio
```

或者复制已有的本地目录：

```bash
cp -R slide-studio ~/.claude/skills/slide-studio
```

## 使用

```text
# 生成——直接说：
用 slide-studio 做一个关于「……」的 slide

# 打磨——打开生成的 .html：
E  改文字        O  排序 / 增删
G  AI 背景       ← → / 空格  翻页        ?s=5  打开第 5 页

# 收工——排序面板里「导出 HTML」，或跑 PDF / Vercel 脚本
```

## 快捷键

| 按键 | 作用 |
|---|---|
| `←` `→` / 空格 / 滚轮 | 翻页 |
| `E` | 改文字（选中后用格式条调字号 / 层级 / 行距） |
| `O` | 排序面板：排序 · 新增 · 复制 · 删除 · 导出 HTML |
| `G` | 图片 / API 设置（可选） |
| `?s=5` | 打开第 5 页 |

## 为什么好看

内置一套规则（见 [`references/design-rules.md`](references/design-rules.md)）：先定设计系统；文字永远叠在图之上、绝不烤进图里；一段共用「风格咒语」让所有图统一；围绕留白构图；先出一张图验证再批量生成。

## 可选工具依赖

生成的 HTML 本身没有运行时依赖，可以离线打开。部分可选流程需要额外工具：

- PPTX 提取：Python 和 `python-pptx`。
- PDF 导出：Node.js、`npx` 和 Playwright/Chromium。
- Vercel 部署：Vercel CLI，并且需要登录 Vercel。
- 网页字体：模板在线加载 Google Fonts 和 jsDelivr；断网时会回退到本机字体。

## 致谢与许可

基于 **frontend-slides**（MIT © 2025 Zara Zhang）构建——其中的模板包与导出脚本一并收录于此，出处见 [NOTICE.md](NOTICE.md)。设计规则整理自 *Isa does AI* 的《How to Vibe Code AI Slides》。

[MIT](LICENSE) © 2026 Ying-A1
