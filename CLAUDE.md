# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project identity

社会学考研笔记整理项目。将教材《社会学概论第2版》（人民出版社2020，马工程重点教材）按网课教授的六要素框架压缩为结构化笔记，供用户背诵答题。

角色：**压缩师，非内容创作者**。只做串联精简，不改写原文。

## Key external paths

教材和所有材料在 repo 外的桌面文件夹，压缩输出也到该处：

| 路径 | 内容 |
|------|------|
| `C:\Users\张庆智\Desktop\助手整理\` | 所有工作材料（教材、网课、用户笔记、初筛输出） |
| `C:\Users\张庆智\Desktop\助手整理\社会学概论第2版 [1-200].docx` | 教材前半（导论—第X章） |
| `C:\Users\张庆智\Desktop\助手整理\社会学概论第2版 [201-440].docx` | 教材后半 |
| `C:\Users\张庆智\Desktop\助手整理\初筛笔记\` | 压缩输出目录，按章建子文件夹 |
| `C:\Users\张庆智\Desktop\助手整理\笔记整理 文字稿.doc` | 网课文字稿（熊宇君讲授） |

Python 路径：`C:\Users\张庆智\AppData\Local\Programs\Python\Python312\python.exe`（Windows Store stub 不可用，必须用此路径。pip 已安装但 python-docx 下载失败，当前用标准库 zipfile + re 解析 docx。）

Memory 文件：`C:\Users\张庆智\.claude\projects\D--Projects-sociology-notes\memory\sociology-note-workflow.md`（流程、进度、角色详述）。

## Compression standard

**严格遵循** `概论六要素压缩标准.md`（v2.0），这是压缩操作的唯一执行标准。核心规则：

- **六要素固定顺序**：①内涵（定义）→ ②特征 → ③外延（类型）→ ④功能/原因与机制 → ⑤视角 → ⑥变迁。笔记中必须按此顺序排列，不管原文顺序。
- **标记**：`★` 核心句（可背可引）、`·` 衔接句（辅助理解）、`⚠` 缺口（教材缺失维度）。仅用于内容行，不用于标题。
- **忠实原文** > 框架完整：教材确实没有的，宁标 ⚠ 不编造。
- **定义优先**：每个概念必须先有 ① 再展开 ②。定义判定标准是能拆出"属+种差"。
- 每节末尾固定留 `✏️ 网课补充` 和 `💭 你的思考` 空白区。

## Extracting text from docx

教材是 .docx 格式。用 Python 标准库提取：

```python
import zipfile, re
with zipfile.ZipFile(docx_path) as z:
    with z.open("word/document.xml") as f:
        xml = f.read().decode("utf-8")
text = re.sub(r'<[^>]+>', ' ', xml)
text = re.sub(r'\s+', ' ', text).strip()
```

注意：docx 提取的文本中 TOC（目录）和正文都会出现章节标题。找正文时跳过第一次出现的章节标题（TOC 条目），取第二次出现开始的内容。用 `str.find('第X章...', first_occurrence + 1)` 定位正文起点。

## Output conventions

- 每节一个 `.md` 文件，放在 `初筛笔记/第X章 XXX/第X节 XXX.md`
- 文件名和目录名与教材章节标题一致
- 每节内按概念分块，每块按六要素框架标注
- 板块划分优先跟随教材自然分节标题；教材无子标题时按概念单元自行划分

## Working with the user

- 用户逐章提供材料，逐章压缩
- 流程调整以用户反馈为准，不在无反馈时自行修改标准
