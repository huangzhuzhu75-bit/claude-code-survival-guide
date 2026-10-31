# Claude Code 稳定使用指南

> 我用了一个月 Claude Code Pro，顺手把折腾过的环境、认证、订阅问题，以及 X 和 GitHub 上值得收藏的工具整理到这里。别再一出问题就换节点、重装软件，先把问题找出来。—— **bobopig**

[**English**](README.en.md) · [快速开始](docs/00-start-here.md) · [提交经验](CONTRIBUTING.md) · [更新记录](CHANGELOG.md)

![Claude Code 使用指南封面](assets/cover.png)

**这是什么？** 一份持续更新的 Claude Code 使用与故障排查知识库：从 Agent 选择，到网络诊断、本地凭据检查、订阅支付及常见错误。文档开放阅读，代码和参考来源都能追溯。

**这不是什么？** 不是 Anthropic 官方教程，不提供节点、账号、代充，也不承诺“100% 不封号”。CheckCC 一类检测工具不是官方风控系统；我的 Pro 正常使用一个月，仅代表我自己的经历。

## 别翻半天，直接找你需要的

- **第一次接触 Claude Code？** → [从这里开始](docs/00-start-here.md) · [Claude Code、Cursor、OpenCode、Grok Bot 怎么选](docs/01-agents.md)
- **网页能用，CLI 报错？** → [终端认证与常见故障](docs/05-troubleshooting.md)
- **想排查 DNS / IPv6 / WebRTC？** → [网络与 AgentRoute 实操](docs/02-network.md)
- **电脑上用过 CC Switch / 旧账号？** → [本地环境和凭据审计](docs/03-local-audit.md)
- **准备订阅 Pro 或升级 Max？** → [注册、付款与使用节奏](docs/04-account-subscription.md)
- **在意遥测和隐私？** → [隐私控制与数据审计](docs/06-privacy.md)
- **只想收藏 GitHub 项目？** → [工具箱](tools/README.md)
- **想知道参考谁的内容？** → [特别感谢与原始链接](references/CREDITS.md)

## 先做一次只读自检

不想手动找一堆设置，可以先运行仓库自带的 Python 检查脚本（Python 3.9+）：

```bash
python scripts/check_env.py
```

它只报告系统、语言、时区、关键环境变量**是否存在**、Claude 配置目录是否存在；默认不访问外部网络、不删除文件、不输出 API Key、Cookie 或完整 IP。

如果需要额外检查 **Python 当前进程**看到的网络地区：

```bash
python scripts/check_env.py --network
```

`--network` 的出口**不一定**等于浏览器或 Claude Code CLI 的出口，三个应用请分别核对。详细用法见 [脚本说明](scripts/README.md)。

## 我的使用顺序

> 先定地区与官方可用性 → 检查网络和系统 → 排查旧认证 → 正常注册 → 确认客户端和订阅 → 再开始长期开发。

我自己偏向日区、自建 VPS 与稳定出口，订阅上先 Pro 再根据需要考虑 Max；平常习惯在额度接近 **80%–90%** 时暂停非必要任务。这些是**个人习惯**，不是 Anthropic 发布的风控阈值。具体写在 [注册、订阅与使用节奏](docs/04-account-subscription.md)。

## 这份仓库怎么更新？

1. 有新工具、规则变化或新问题，我会先更新对应章节，避免在 README 塞一堆重复内容。
2. 每次重要调整记录在 [CHANGELOG](CHANGELOG.md)。
3. 欢迎通过 GitHub Issues 或 PR 交流，**不要贴 Token、Cookie、真实 IP、账号邮箱、账单全图**。
4. GitHub 是开放技术资料库；飞书更适合阅读、整理和交流。飞书文档入口发布后会补在这里：**（待填写）**。

## 资料版权

原创教程采用 [CC BY 4.0](LICENSE-CONTENT.md)，仓库自写脚本采用 [MIT](LICENSE-CODE)。第三方软件、脚本及资料**只附链接，不重新授权、不冒充原创**。详细鸣谢：[references/CREDITS.md](references/CREDITS.md)。

[**如何发布到 GitHub？**](PUBLISHING.md)

**作者：bobopig · v1.0.0 · 2026-11-01**
