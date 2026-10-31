# 00｜先看这里：十分钟定位问题

[返回首页](../README.md) · [下一篇：Agent 选择](01-agents.md)

先说我的思路：**别乱改设置，一次只处理一个变量。** 你甚至可以不安装任何额外工具，先按下面顺序排查。

## 第一步：分清是哪种故障

- **网页打不开**：先看浏览器、DNS、网络出口和服务可用性。
- **网页能用、CLI 不行**：优先查 CLI 的认证方式、`ANTHROPIC_*` 与代理环境变量。
- **浏览器和终端表现不同**：分开看系统代理、TUN、IPv6、DNS。
- **付款或续费失败**：先看真实订单、平台订阅、支付渠道，不要连续重付。
- **账号明确 Suspended / Disabled**：先保存报错和订阅资料，走官方支持流程；不要把网络报错和封号混成一回事。

## 第二步：本机只读检查

```bash
python scripts/check_env.py
```

脚本只检查环境变量名称是否存在，不打印值。Windows PowerShell 也可以直接用：

```powershell
Get-ChildItem Env:ANTHROPIC* | Select-Object -ExpandProperty Name
Get-ChildItem Env:*PROXY* | Select-Object -ExpandProperty Name
Test-Path "$HOME\.claude.json"
Test-Path "$HOME\.claude"
```

如果看到 `ANTHROPIC_API_KEY`，而你本来想走 Pro/Max 订阅登录，先去 Claude Code 的 `/status` 确认是否意外走了 API 计费。官方说明：[API Key 环境变量优先级](https://support.claude.com/en/articles/12304248-manage-api-key-environment-variables-in-claude-code)。

## 第三步：需要时再查网络

按实际情况检查 [网络篇](02-network.md) 里的 HTTPS、DNS、IPv6 和 WebRTC；遇到配置错误，**先备份、再修改、再复测**。

## 第四步：遇到故障直接跳章节

- [网络与 AgentRoute](02-network.md)
- [本地认证 / 旧凭据](03-local-audit.md)
- [订阅与支付](04-account-subscription.md)
- [常见故障速查](05-troubleshooting.md)

**不需要做的事**：只因为检测分数不漂亮就重装系统、抹掉全部 `.claude`、换一堆节点或复制陌生脚本执行。先搞清问题落在哪一层。
