# 05｜出问题先看这里：Claude Code 常见故障

[返回首页](../README.md)

不用一报错就换账号。这张速查卡按**症状**来，不按“听说某个 IP 被拉黑”来猜。

## A. 网页正常，Claude Code CLI 报错

先在 CLI 里确认当前认证：

```text
/status
```

然后在 Windows PowerShell 里执行：

```powershell
Get-ChildItem Env:ANTHROPIC* | Select-Object -ExpandProperty Name
Get-ChildItem Env:*PROXY* | Select-Object -ExpandProperty Name
```

macOS / Linux：

```bash
printenv | cut -d= -f1 | grep -E '^(ANTHROPIC_|HTTP_PROXY|HTTPS_PROXY|ALL_PROXY)'
```

有 `ANTHROPIC_API_KEY` 可能导致 API 优先计费，见 [官方帮助](https://support.claude.com/en/articles/12304248-manage-api-key-environment-variables-in-claude-code)。再对照代理模式、TUN、DNS 和实际 CLI 请求路径。

## B. 403 / 地区不可用 / 连接突然失败

区分 403 是 Anthropic 本身返回，还是代理、公司网关、WAF、浏览器扩展返回。记下**完整报错文本中的非敏感部分**、发生时间、客户端和当前网络模式；先查网络路径，不要立即认定封号。如果账号明确显示 Suspended / Disabled，再走官方支持。

## C. IP 检测正常，但 DNS 或 WebRTC 显示其他地址

检查浏览器独立 DoH、客户端 DNS 规则、IPv6、WebRTC UDP 与 TUN 接管；按 [网络篇](02-network.md) 的检测步骤逐项记录。不要只看某个网站有没有给“高分”。

## D. 新登录总回到旧账号

退出相关客户端，检查浏览器站点数据、本地旧 OAuth、Windows 凭据管理器或 macOS 钥匙串。先备份再清理，参见 [本地篇](03-local-audit.md)。

## E. 订阅扣款了，但权益没有更新

先核对实际订单、扣款账户、订阅所属账号，再看 App Store / Google Play / 网页端权益同步与恢复购买。保存订单号，必要时找对应平台客服。

## F. KYC 或账号暂停

- KYC：按页面真实验证；保存截图，不要反复提交不一致的资料。
- Suspended / Disabled：优先使用官方支持/申诉；对来自 Apple/Google 的订阅，另外确认自动续费。

## 我排查时的五条规矩

1. 先保留报错和时间戳，不上传 Cookie、Token、完整 IP。
2. 一次只改一个变量，避免最后不知道改好了哪一步。
3. 更新代理规则前先备份、再做原生语法检查。
4. 任何“还没测”的项目都写 **未验证**。
5. 一个工具能检查某个网络信号，不代表它能预测账号处置。
