# 华硕小二项目规则（入库版，无密码）

项目级规则优先于系统级。账号密码用本机凭据，不写进仓库。

## 无痕窗口

每个测试环境独立 browser context，cookie 隔离、互不串号。

- `newctx` / `usectx` / `ctxlist` / `disposectx`
- 环境名：`xiaoe`（小二后台）、`cs-presale` / `cs-bus` / `cs-after`（客服三端）、`bus-user`（企业购用户端）
- Chrome 重启后无痕会话丢失，需重新登录

## 入口（地址可写，密码不写）

| 端 | 地址 | 登录 |
|---|---|---|
| 小二管理后台 | https://dev-asus.njsyue.com/sxr/web/index.html#/staff-admin | 图形验证码 |
| 客服 | https://dev-asus.njsyue.com/cs/web/web/index.html#/login | 图形验证码；售前 / 企业购 / 售后三账号同源，无痕窗口才能并行 |
| 企业购用户端 | https://dev-mall-bus.njsyue.com | 短信验证码；密码登录实测被拒绝 |

验证码：页面取原图 → 放大 → 人工确认。不试错。

## 数据

新建前说明内容，同意后再写。命名 `wwd_` + 日期，登记台账，默认保留。禅道只读。
