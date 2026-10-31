# 06｜隐私与遥测：Claude Code 在后台做什么？

[返回首页](../README.md)

我把遥测和封号分成两件事：**了解客户端收集什么、能配置什么，是隐私管理；不等于关掉遥测就能防封号。**

值得研究的项目：

- [B1anYu / claude-telemetry-audit](https://github.com/B1anYu/claude-telemetry-audit)：Claude Desktop、Code、Android 数据行为的技术研究。
- [AschoofAlpha / claude-sonar](https://github.com/AschoofAlpha/claude-sonar)：本地网络、隐私和配置一致性审计。
- [Anthropic 官方数据使用说明](https://code.claude.com/docs/en/data-usage)
- [Anthropic 官方设置说明](https://code.claude.com/docs/en/settings)

Claude Code 可按需使用的环境变量示例（不是要求所有人必须开启）：

```json
{
  "env": {
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
  }
}
```

可以把对应字段**合并**到 `~/.claude/settings.json` 里的顶层 `env`，不要直接覆盖现有设置。修改后重启客户端。某些开关会影响功能开关获取或远程控制，启用前先阅读官方说明。

需要注意：客户端推理请求、更新检查、反馈功能及不同平台的数据处理机制各有区别。“关闭可选遥测”不等于“零数据上传”，也不是完整匿名化。

我不会在公开 Issue 里收集任何人的登录凭据、真实网络地址或账单。
