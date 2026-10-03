#!/usr/bin/env python3
"""把用户的 GitHub Star 列表同步为 starred/README.md（分类整理）.

用法: python tools/gen_stars.py
本脚本既用于本地首次生成，也被 .github/workflows/sync-stars.yml 定时调用。
"""
import json
import urllib.request
from datetime import datetime, timezone, timedelta

USERNAME = "dhao36-cloud"
OUT_PATH = "/home/hatch/workspace/starsync/starred/README.md"

CATEGORIES = [
    ("AI 大模型与智能体", ["llm", "claude", "agent", "skill", "mcp", "gpt", "codex",
                          "notebooklm", "chatgpt", "ai ", " ai", "artificial"]),
    ("音视频创作与处理", ["video", "sora", "montage", "resolve", "voice", "tts",
                          "elevenlabs", "剪映", "jianying", "影视", "reclip",
                          "seal", "gofilm", "vip视频", "media-downloader", "videovip",
                          "video_vip"]),
    ("网络与代理", ["proxy", "sing-box", "nekobox", "fanqiang", "翻墙", "vpn", "科学上网"]),
    ("Android 应用", ["android", " tv", "tv直播", "kotlin"]),
    ("阅读与学习", ["textbook", "ebook", "教材", "电子书", "english", "英语",
                    "congshu", "丛书", "book"]),
    ("投资理财", ["stock", "quant", "trading", "股票", "基金", "terminal"]),
    ("效率工具", ["白板", "whiteboard", "markdown", "markitdown", "cleaner",
                  "disk", "news", "新闻", "网盘", "linkswift", "drawnix", "kudu"]),
    ("开发资源", ["awesome-python", "awesome-"]),
]


def fetch_starred(user):
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/users/{user}/starred?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={"User-Agent": "star-sync",
                                                  "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            batch = json.load(resp)
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fmt_stars(n):
    if n >= 1000:
        s = f"{n / 1000:.1f}"
        if s.endswith(".0"):
            s = s[:-2]
        return s + "k"
    return str(n)


def categorize(repo):
    hay = (repo["full_name"] + " " + (repo.get("description") or "")).lower()
    for title, keywords in CATEGORIES:
        if any(k in hay for k in keywords):
            return title
    return "其他"


def main():
    repos = fetch_starred(USERNAME)
    groups = {}
    for r in repos:
        groups.setdefault(categorize(r), []).append(r)
    # 类别按预设顺序, 其他放最后; 组内按 star 数降序
    order = [c[0] for c in CATEGORIES] + ["其他"]
    bj = timezone(timedelta(hours=8))
    now = datetime.now(bj).strftime("%Y-%m-%d %H:%M")
    lines = [
        "# ⭐ Star 收藏夹",
        "",
        f"共 {len(repos)} 个仓库，由 GitHub Actions 每周自动同步（最后同步：{now} 北京时间）。",
        "手动刷新：在仓库 Actions 页运行「同步 Star 列表」工作流。",
        "",
    ]
    for title in order:
        items = groups.get(title)
        if not items:
            continue
        items.sort(key=lambda r: r.get("stargazers_count", 0), reverse=True)
        lines.append(f"## {title}（{len(items)}）")
        lines.append("")
        for r in items:
            desc = (r.get("description") or "").strip().replace("\n", " ")
            lang = r.get("language") or ""
            meta = f"⭐ {fmt_stars(r.get('stargazers_count', 0))}"
            if lang:
                meta += f" · {lang}"
            line = f"- [{r['full_name']}]({r['html_url']})"
            if desc:
                line += f" — {desc}"
            line += f"（{meta}）"
            lines.append(line)
        lines.append("")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"wrote {OUT_PATH} with {len(repos)} repos in {len(groups)} groups")


if __name__ == "__main__":
    main()
