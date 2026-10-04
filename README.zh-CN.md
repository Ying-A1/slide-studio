# slide-studio

> 用对话让 AI 做出好看、**可编辑**的幻灯片 —— 然后在浏览器里排序、换皮、改字号层级行距，还能（可选）配上 AI 生成的背景。

[English](README.md) · **中文说明**

`slide-studio` 是一个 [Claude Code / Agent **Skill**](https://docs.claude.com/en/docs/claude-code/skills)。
它生成**单文件、零依赖、固定 16:9** 的 `.html` 幻灯片，并自带一个真正能用的浏览器内编辑器。
它是 Zara Zhang 的 [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) 的**超集** ——
它有的功能全都有，另外补上了纯 HTML 幻灯片一直缺的编辑能力；设计规则取自 YouTube 教程
*《How to Vibe Code AI Slides》*（作者 **Isa does AI**）。

## 功能

`frontend-slides` 有的：

- 🧱 **零依赖** —— 一个 HTML 文件，内联 CSS/JS，无需构建。
- 🎨 **"show, don't tell" 选风格** —— 从生成的可视化预览里挑；内置[预设](references/STYLE_PRESETS.md)
  + **34 套** [bold 模板包](bold-template-pack/)。
- 📥 **PowerPoint 转网页** —— 转换 `.pptx`，保留文字、图片、顺序与备注。
- 🖨️ **导出** —— PDF（`scripts/export-pdf.sh`）或 **Vercel** 在线链接（`scripts/deploy.sh`）。
- 🖼️ **固定 16:9**、动效丰富、可访问、拒绝"AI 味"。

slide-studio 另外补上的：

- ✍️ **就地改字** —— 点任意文字直接编辑。
- 🔤 **改字号 / 层级 / 行距** —— 浮动格式条，不用写代码。
- ↕️ **排序 / 新增 / 删除 / 复制幻灯片** —— 拖拽式管理面板。*（纯 HTML 幻灯片一直缺这个。）*
- 🤖 **可选 AI 背景** —— 用你**自己的**图像 API 生成电影感背景。完全可选；不配就用 CSS 渐变，一样好看。仓库里不含任何密钥。
- 🎬 **动效** —— 错峰入场 + 图片页缓慢 Ken-Burns 推镜。
- ⬇️ **导出干净的单文件 `.html`**，把新顺序 / 编辑 / 字号都固化进去。

## 安装

```bash
cp -R slide-studio ~/.claude/skills/slide-studio
```

然后对它说：*"用 slide-studio 做一个关于……的 slide"*。

## 设计规则（为什么好看）

由 Skill 强制执行，详见 [`references/design-rules.md`](references/design-rules.md)：

1. **先定设计系统** —— 一个底色、一个文字色、一个强调色；一个标题字体 + 一个正文字体。
2. **图里绝不烤字** —— 文字 / 数字 / 图表都叠在图之上；图里不含 logo 或文字。
3. **一段共用"风格咒语"** 追加到每条生图提示词末尾 → 全套同一种美术风格。
4. **围绕文字构图** —— 指明空哪一侧、主体推到另一侧、重要元素放画面中间 2/3（手机 / PDF 会裁边）。
5. **亮、可读、语义化** —— 可读的背景、图表放独立面板、颜色自带含义。
6. **先出第一张图验证，再批量。**

## 可选：AI 背景图（需自己开启）

除非**你**自己配置了图像 API，Skill 不会生成任何图片。两种方式：

- **浏览器里**：在幻灯片里按 **`G`**，粘贴 OpenAI 兼容的 **Base URL + Key + Model**，写一句画面描述，点生成。
  配置只存在你本地浏览器的 `localStorage`。
- **用脚本**：

```bash
export IMAGE_API_BASE="https://your-endpoint/v1"
export IMAGE_API_KEY="sk-..."        # 你的密钥 —— 绝不入库
export IMAGE_MODEL="gpt-image-2"
python scripts/gen_image.py "云海之上的浮空城，左侧留白，无文字" out/cover.png
```

详见 [`references/image-generation.md`](references/image-generation.md)。

## 快捷键（在生成的幻灯片里）

| 按键 | 作用 |
|---|---|
| `←` `→` / 空格 / 滚轮 | 翻页 |
| `E` | 编辑模式（随后用格式条调字号 / 层级 / 行距） |
| `O` | 排序面板 —— 拖拽或 ↑↓ 排序、新增、复制、删除、**导出 HTML** |
| `G` | 图片 / API 设置（可选） |
| `?s=5` | 直接打开第 5 页 |

## 致谢与许可

- 是 **frontend-slides** 的超集（MIT © 2025 Zara Zhang），并沿用了其部分文件 —— 见 [NOTICE.md](NOTICE.md)。
- 设计规则取自 *Isa does AI* 的 **《How to Vibe Code AI Slides》**（独立复刻，无从属关系）。

[MIT](LICENSE) © 2026 Ying-A1
