# 02｜网络与连接路径：VPS、DNS、IPv6、WebRTC、AgentRoute

[返回首页](../README.md) · [工具箱](../tools/README.md)

**别只查 IP。** 浏览器、终端、DNS、IPv6 和 WebRTC 可能走不同路径。我个人偏向自建 VPS、稳定网络出口，也用过搬瓦工；但 VPS 不等于住宅 IP，所谓“干净 IP”没有统一的官方认证标准。

## 1. 先记录真实情况

- 当前所在地区是否受服务支持；网络出口、ASN、运营商是什么。
- 代理模式：系统 HTTP 代理、TUN / VPN，哪个生效？
- CLI 是否继承了 `HTTP_PROXY` / `HTTPS_PROXY` / `ALL_PROXY`。
- 配置来自本地文件，还是订阅刷新后会被覆盖？
- IPv4 和 IPv6 是否都被接管；浏览器有没有独立“安全 DNS”。

建议分别在**同一个网络状态**下检查：浏览器、Claude Code CLI、手机。不要为了测试随手断开正在使用的代理。

### HTTPS / IPv4 / IPv6

Windows PowerShell：

```powershell
curl.exe -4 https://www.cloudflare.com/cdn-cgi/trace
curl.exe -6 https://www.cloudflare.com/cdn-cgi/trace
```

macOS / Linux：

```bash
curl -4 https://www.cloudflare.com/cdn-cgi/trace
curl -6 https://www.cloudflare.com/cdn-cgi/trace
```

输出里有实际公网 IP，**别在公开 Issue 里原样粘贴**。IPv6 请求失败可能只是当前网络没有 IPv6，不等于“安全通过”。

## 2. DNS：不是把 DNS 关闭

浏览器里的安全 DNS（DoH）可能独立于代理客户端的 DNS 规则。我的做法是先搞清楚哪个组件负责解析，避免规则重叠或某条路径意外直连。

Mihomo / Clash Meta 模板中几个值得理解的字段：

```yaml
# 示例字段，仅作原理说明；不是完整配置，不能直接覆盖订阅。
dns:
  enable: true
  enhanced-mode: fake-ip
  respect-rules: true
  nameserver:
    - https://1.1.1.1/dns-query#PROXY
```

`PROXY` 是占位符，**必须替换成你自己真实存在的代理组**。完整模板涉及节点域名引导解析、内网例外、备用解析器、sniffer 和规则顺序，直接参考 [AgentRoute / Mihomo 完整模板](https://github.com/ryuu-restart/agent-route/blob/master/examples/full/mihomo.yaml)，不要只复制上面几行就说配置完成。

注意：DoH 是**加密 DNS 查询**，不等于查询一定经过你的代理。

## 3. WebRTC / STUN

普通网页出口正常，不说明实时通信的 UDP 路径已经按预期接管。可以检查：

- [BrowserLeaks WebRTC](https://browserleaks.com/webrtc)
- [Trickle ICE](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/)

Chrome / 部分 Chromium 浏览器可以使用 [WebRTC Network Limiter](https://chromewebstore.google.com/detail/webrtc-network-limiter/npeicpdbkakmehahjeeohfdhnlpdklia)，在扩展的设置里选择 `Disable non-proxied UDP`。变更后要重新测试 ICE 候选以及你常用的音视频业务。**检测页面没输出候选，不等于没有泄漏**，也可能是 STUN 根本不可用。

## 4. 重点项目：AgentRoute

GitHub：[ryuu-restart/agent-route](https://github.com/ryuu-restart/agent-route)

- [Agent 执行入口](https://github.com/ryuu-restart/agent-route/blob/master/AGENTS.md)
- [客户端接入说明](https://github.com/ryuu-restart/agent-route/blob/master/docs/CLIENTS.md)
- [DNS / WebRTC 验收指南](https://github.com/ryuu-restart/agent-route/blob/master/docs/DNS-WEBRTC.md)
- [Mihomo 完整模板](https://github.com/ryuu-restart/agent-route/blob/master/examples/full/mihomo.yaml)

项目提供 Mihomo、Surge、Shadowrocket、sing-box 等格式的规则与模板，**不提供代理节点**。不同客户端和核心版本不能无脑互相套用。

### 我给 Codex 的完整执行提示词

```text
请先阅读以下项目，而不是只看首页：
https://github.com/ryuu-restart/agent-route
https://github.com/ryuu-restart/agent-route/blob/master/AGENTS.md
https://github.com/ryuu-restart/agent-route/blob/master/docs/CLIENTS.md
https://github.com/ryuu-restart/agent-route/blob/master/docs/DNS-WEBRTC.md

第一步（只读）：确定系统、客户端和真实内核版本、配置来源、节点/代理组、系统代理或 TUN、DNS、IPv6、浏览器安全 DNS、现有规则和例外。

第二步（方案）：说明哪些配置要改、改动放哪里才不会被订阅刷新覆盖，备份所有将修改的文件。认证信息、节点和原有例外必须保留。

第三步（修改）：经我确认后才接入对应版本的模板。不要覆盖整份订阅，不要随意关闭代理或切换节点，不要绕过企业设备策略。

第四步（验证）：运行原生配置检查，然后验证规则加载、HTTPS 出口、DNS 解析出站、IPv4/IPv6、WebRTC 候选、Claude Code CLI 的实际路由。刷新一次订阅，重启客户端复查。

第五步（报告）：列出修改文件、备份路径、规则版本、每项验证结果、未验证事项，以及具体回退步骤。不要在报告里打印 Token、密码或完整 IP。
```

### 各客户端最容易踩的坑

- **Clash Verge Rev**：订阅管理的配置不要直接手改后就忘了，下次更新可能覆盖；优先看扩展配置与规则编辑。
- **Mihomo**：确认 `dns.respect-rules`、节点引导解析、真实主代理组名称、IPv6 与 FakeIP 排除项；配置更新后使用内核检查。
- **Surge**：DNS 出站与规则匹配机制和 Mihomo 不同，不能直接照搬 YAML。
- **Shadowrocket**：设备上的版本和实际导入行为需要人工测试，项目的示例模板并不保证每台 iPhone 都已验证。
- **sing-box**：字段版本变化较快，要核对模板所需内核版本。

## 5. 测试完成算什么？

每次修改只回答五件事：**改了什么、浏览器出口是什么、CLI 出口是什么、DNS/WebRTC 是否复查、如何回退。**

不要因为一个检测网站打了高分，就把它当作账号不会被封的证明；这些检查主要用于**确认连接路径和排查配置故障**。
