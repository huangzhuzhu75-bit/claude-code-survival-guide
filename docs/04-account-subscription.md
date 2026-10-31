# 04｜注册、Pro / Max、付款与我的使用节奏

[返回首页](../README.md)

先声明：我本人使用 **Claude Code Pro 一个月**，暂时没有遇到封禁。这是个人经历，不是“照着做就能保证不封”。

## 我的实际顺序

**1. 先确认长期使用地区及服务可用性。** 我自己主要使用日区环境。手机号、邮箱、订阅地区和实际账号资料尽量提前确认，使用真实、可恢复的身份信息。

**2. 选择自己能长期控制的付款方式。** 安卓看 Google Play，iOS 看 App Store，网页端按官方结算页面来。第三方代充可能带来退款、订单归属和后续售后问题，我个人不喜欢。

**3. 网络先配置好。** 我偏向自建 VPS 和固定网络出口；住宅 IP 是我个人偏好，**不是官方认证的“保号凭证”**。具体检查方式见 [网络篇](02-network.md)。

**4. 设备按真实使用环境设置。** 系统时区、语言和浏览器配置要可解释、稳定。DNS 主要检查路径是否正确，而不是“一键关闭浏览器 DNS”。

**5. 用过旧账号或网关的机器，先检查旧认证。** 不需要为了“清空痕迹”重置整个系统；旧数据处理见 [本地审计](03-local-audit.md)。

**6. 注册前后做一次必要检查。** 我最早用 [IPKK](https://ipkk.com)，后来更常看 [CheckCC](https://checkcc.org) 等综合工具。检查的是配置是否正常，不是后台风控分数。

**7. 正常注册，妥善保存恢复方式。** 不买来路不明的共享号，不随意借用他人的支付资料。

**8. 新账号我不会第一分钟就冲最贵套餐。** 我个人习惯先正常聊几天（常见是 1–3 天，不着急就一周），看看登录和基础功能是否稳定。有人把这个叫“养号、信用分”，但 Claude 并没有对普通用户公开可核对的信用分或固定养号周期。

**9. 能稳定使用的账号，我不爱反复折腾。** 如果遇到 KYC，按照页面要求使用真实资料完成身份验证；别把“跳 KYC”一律理解成账号已经死亡。

**10. 先 Pro，觉得额度真不够再升级 Max。** 我更偏好先按实际任务消耗决定档位；Pro/Max 订阅的 OAuth 登录和 Anthropic API Key 是**两套不同的认证及计费体系**，不要把多个个人订阅凭据拼成一个所谓公共 API 池。

**11. 我自己的额度纪律：用到大约 80%–90% 就暂停非必要任务。** 这只是我的工作流习惯，给突发任务留余量，不是官方公布的安全阈值。

## 订阅前别漏掉三件事

- **订单归谁管？** App Store、Google Play 和官方网页的订阅管理、退款入口不同。
- **有没有真的扣款？** 如果失败先查订单，不要连点十次。
- **实际走什么认证？** CLI 用 `/status` 核对 API 还是订阅登录。 [官方说明](https://support.claude.com/en/articles/12304248-manage-api-key-environment-variables-in-claude-code)。

## 支付失败 / KYC / 暂停

**iOS 购买失败**：在系统订阅管理核对套餐及订单；Apple 官方支持：[getsupport.apple.com](https://getsupport.apple.com)。

**KYC**：记录具体要求及发生时间，使用本人的真实信息按页面步骤操作，必要时联系官方支持。

**Suspended / Disabled**：保留报错信息、注册邮箱、支付订单时间、客户端版本，按官方申诉路径处理，同时确认自动续费有没有继续。

### 给客服的英文模板

> Hello, I’m trying to upgrade my Claude subscription through the App Store, but the purchase could not be completed. My current plan is [current plan], and I’d like to switch to [target plan]. Could you please check my purchase status and advise on the next steps? Thank you.

## 最后一句

**别为了一个所谓完美配置花掉全部开发时间。** 账号合规、网络可排查、订单可管理、真正能持续做项目，才是我在意的。
