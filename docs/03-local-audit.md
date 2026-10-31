# 03｜本地环境与旧凭据：先审计，别直接 rm

[返回首页](../README.md) · [脚本说明](../scripts/README.md)

用过多个账号、API Key、CC Switch、OpenCode 或其他网关以后，Claude Code 有时会读到旧设置。我的原则是：**先看清当前真正生效的认证，再决定删什么。**

## Windows：先执行这些只读命令

打开 PowerShell：

```powershell
# 只列变量名，不输出秘钥内容
Get-ChildItem Env:ANTHROPIC* | Select-Object -ExpandProperty Name
Get-ChildItem Env:*PROXY* | Select-Object -ExpandProperty Name

# 本地 Claude 配置目录是否存在
Test-Path "$HOME\.claude.json"
Test-Path "$HOME\.claude"

# 系统时间、语言
Get-TimeZone
Get-Culture
```

还可以人工检查 Windows 凭据管理器、Chrome/Edge 的 Claude 网站数据，以及 VS Code / Claude Desktop 当前是否登录旧账号。**不要把 `.claude` 全目录当缓存删掉**：里面可能有项目历史、Skills、Hooks、MCP 等。

## macOS / Linux

```bash
# 代理配置、时区
scutil --proxy    # macOS
# macOS：sudo systemsetup -gettimezone（需要相应权限）

# 仅列变量名，不输出 Key 或 Token
printenv | cut -d= -f1 | grep -E '^(ANTHROPIC_|HTTP_PROXY|HTTPS_PROXY|ALL_PROXY)'

# 目录是否存在
ls -ld ~/.claude ~/.claude.json 2>/dev/null
```

macOS 的钥匙串中可能保存 Claude Code 的历史认证；检查之前先退出相关程序，确保有备份。

## 一次查完三端：本仓库的只读脚本

```bash
python scripts/check_env.py
```

需要了解**当前 Python 进程**看到的公网地区，再加 `--network`。详细边界见 [scripts/README.md](../scripts/README.md)。

## 比较成熟的清理 / 审计项目

**夙愿 Claude Cleanup**：[SKILL.md](https://github.com/suyuan2022/suyuan-skill/blob/main/claude-cleanup/SKILL.md)。提供审计、备份、选择性清理的路线。按作者说明操作，优先 `--audit`：

```bash
# 在仓库 claude-cleanup 目录里执行
python3 scripts/claude_cleanup.py --audit
```

**pnedfff Claude Env Cleanup**：[GitHub](https://github.com/pnedfff/claude-env-cleanup)。偏向 macOS 本地审计、代理/网络状况、CC Switch 等残留。安装成 Codex Skill 后可以执行：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/pnedfff/claude-env-cleanup.git ~/.codex/skills/claude-env-cleanup
python3 ~/.codex/skills/claude-env-cleanup/scripts/audit_claude_env.py
python3 ~/.codex/skills/claude-env-cleanup/scripts/audit_network_env.py
```

上面是第三方项目本身提供的命令，实际执行前仍应查看仓库 README 和脚本内容。本文**不复制或转售这些项目的脚本**。

## 为什么特别提 API Key？

官方说明：当终端里设置了 `ANTHROPIC_API_KEY`，Claude Code 可能优先使用 API 计费，而不是你以为正在使用的 Pro/Max 订阅。进入 Claude Code 后用 `/status` 确认认证来源，必要时退出旧登录并检查变量。

[Anthropic：Manage API Key Environment Variables](https://support.claude.com/en/articles/12304248-manage-api-key-environment-variables-in-claude-code)

**保留最后一条：所有凭据只在本机检查，公开报告只写“存在 / 不存在”。**
