# 自带脚本：只读 Claude 环境检查

[返回首页](../README.md)

这是我自己整理的一个轻量脚本。用途是列出**当前机器的基本环境信息及配置存在性**，不是测封号概率，也不是替你修改系统配置。

Python 3.9+，无第三方依赖；Windows / macOS / Linux 通用。

```bash
python scripts/check_env.py
```

输出内容：操作系统、Python 版本、时区、地区设置、敏感环境变量是否存在、Claude 配置文件是否存在。**不会输出密钥值。**

可选联网测试：

```bash
python scripts/check_env.py --network
```

联网测试仅查询 Cloudflare Trace，返回当前 Python 进程的地区码和协议类型，不打印公网 IP；网络超时会明确说明。它不能代替浏览器、Claude Code CLI、WebRTC 或 DNS 的独立检测。

可选机器可读输出：

```bash
python scripts/check_env.py --json
```

**隐私提醒**：即使脚本只输出环境变量“存在 / 不存在”，报告也可能暴露你使用某种代理或网关。对外提交 Issue 前请人工复核。

脚本默认不写文件、不执行清理、不修改时区、DNS、代理设置和系统凭据。
