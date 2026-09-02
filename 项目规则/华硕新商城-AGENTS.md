# 项目规则：华硕新商城（项目级专属配置）

> 用例条数/步骤、四件套命名、归档结构、验证码、小程序 CLI、禅道只读、交接文档等一律按系统级规则。测试细则（任务命中才读，不预读）：`%USERPROFILE%\.codex\测试规则\测试规则.md`。本文件只留本项目入口和路径，**项目级优先**。

## 归档

- 根目录：`D:\测试用例\{YYYYMMDD}\{需求名-负责人}\`。第一层只写生成日期，不要再套 `华硕新商城_执行名`。
- 正式交付物以归档目录为准：改用例/状态/证据/手册直接改对应需求文件夹，工作区只留源 JSON（`cases_*.json`）。

## 测试环境入口清单

登录顺序、验证码、同意后再写入：按系统级。账号密码用本机已保存凭据，**不要写进本文件**。

### 新商城（CDP 9222，profile `%TEMP%\codex-browser-profile`，启动 `.codex-build\start_cdp_9222.ps1`）

| 端 | 地址 | 账号 | 登录方式 |
|---|---|---|---|
| 平台后台 | https://dev-mall-admin.njsyue.com | wwd | 图形验证码 + 短信 |
| 商户后台 | https://dev-mall-seller.njsyue.com | wwd | 图形验证码 + 短信 |
| 用户端 PC | https://dev-mall-pc.njsyue.com | 19552261935（会员：wwd测试） | 短信验证码 |
| 用户端 H5 | https://dev-mall-m.njsyue.com | 同上 | 短信验证码 |
| Android App | 真机华硕商城测试包（入口见交接；本机无包仍建条） | 同上 | 按 App |
| iOS App | 真机华硕商城测试包（入口见交接；本机无包仍建条） | 同上 | 按 App |

### 会员商城

| 端 | 地址 | 账号 | 登录方式 |
|---|---|---|---|
| 后台 | https://dev-mbrmkt-admin.njsyue.com | 是否与新商城 wwd 共用见《会话交接.md》 | 按页面 |
| H5 | https://dev-mbrmkt-m.njsyue.com | 同上 | 按页面 |
| Android / iOS App | 真机会员商城测试包（入口见交接；本机无包仍建条） | 同上 | 按 App |

## 接口自动化

- 唯一框架（已从本工作区拆出）：`C:\Users\admin\Desktop\华硕新商城-自动化`（Python + pytest + requests）。对照 `D:\自动化study` 阶段 2。
- 鉴权：复用 CDP 9222 已登录态读 `sld_token`。启动：该目录下 `启动浏览器.ps1`。
- 新接口任务：只在该目录 `tests/` 加 `test_*.py`。不要再在本工作区建第二套框架。
- 本工作区 `.codex-build/*.mjs` 是历史执行/探针，不是现行框架。

## 用例端口

**移动端 = iOS、Android、H5、小程序**，四端默认全测、各自成组。上表「用户端 H5」只是 H5 地址。只有文档原文点名某一端不测才跳过该端。无测试包/无源码仍建条；执行 Android/iOS 走真机配合（王文东真机操作，模型改线上配置后出手机卡）。触及 PC 则 PC 另组。

## 小程序

- 工具路径、服务端口、无源码时的处理：按系统级；当前端口见《会话交接.md》。
- 插件：工作区 `.codex-build\miniprogram-automator`
- 新商城 appid：`wx7f91f632b33a9cc6`；会员商城 appid：`wxdb0ec0f95ef00ef5`
- **本机无源码**，自动化标受阻；小程序用例由王文东在体验版上手测
