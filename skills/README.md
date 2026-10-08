# 🛠️ AI Skill 收藏

> 来源：抖音《AI凭什么替你干活？就凭装对了skill》（2026-10-06）
> 原话："四个装完，AI就不是聊天工具了。"
>
> 下面四个按视频顺序排列，附 GitHub 链接与安装方法。

---

## 1. Computer Use —— 让 AI 接管你的电脑

- **干嘛的**：让 AI 走出聊天框，自己动鼠标、敲键盘、开软件、读写文件，直接操作 Windows。
- **GitHub**：[CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP)（⭐ 7000+）
- **怎么装**：电脑上运行 `uvx windows-mcp serve`，再配到 Claude Code / Codex 的 MCP 配置里即可。
- **备注**：视频里演示的即此类 Computer Use 能力；本仓库 Star 收藏夹中已收录。

## 2. ChatCut —— 让 AI 帮你剪辑视频

- **干嘛的**：AI 连接 ChatCut 桌面端，协助剪视频：导素材、剪时间线、加字幕、配音配乐、导出成片，还能自己上网找素材。
- **GitHub**：[ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin)（官方出品，⭐ 900+）
- **怎么装**：官方插件。把仓库地址直接交给你的 AI 让它按说明安装；Codex 看 [chatcut.io/chatgpt](https://chatcut.io/chatgpt)，Claude Code 看 [chatcut.io/claude](https://chatcut.io/claude)。需要登录 ChatCut 账号。
- **备注**：作者在评论区确认可在 WorkBuddy 里使用。

## 3. Deep Research —— 让 AI 交叉查证、结论带来源

- **干嘛的**：查资料时派出"搜索员"，多源检索、交叉验证，每个结论都带来源链接，避免 AI 一本正经地胡说。
- **GitHub**：候选 [trojanbox/agent-plugin-marketplace](https://github.com/trojanbox/agent-plugin-marketplace) 内 `plugins/research/skills/deep-research/SKILL.md`
- **怎么装**：标准 SKILL.md 结构，拷到 Agent 的 skills 目录（如 `~/.claude/skills/`）即可调用。
- **备注**：⚠️ 视频画面中的确切仓库名未能读取（作者提示"读大图片，可以看到"，约在视频 01:10 处）。此处为同名候选，请以原视频画面为准。

## 4. cangjie-skill —— 把爆款内容"蒸馏"成你的方法论

- **干嘛的**：把书、长视频、播客、教程甚至大神的决策方式，拆成一套你能直接照做的框架，并做成可被 AI 调用的 skill。
- **GitHub**：[cnfulishe/cangjie-skill](https://github.com/cnfulishe/cangjie-skill)（MIT 协议）
- **怎么装**：标准 skill 结构，拷到 Claude Code 的 skills 目录（Windows：`C:\Users\你的用户名\.claude\skills\`）或 OpenClaw skills 目录，重启即生效。对它说"帮我把《XXX》蒸馏成 skill"即可。
- **备注**：仓库很新，属尝鲜项目；另有配套 video-downloader skill 可先下载视频再蒸馏。

---

*最后更新：2026-10-08。*
