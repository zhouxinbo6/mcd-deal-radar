# 麦麦优惠雷达 Pro（mcd-deal-radar）

> 麦当劳程序员创意开发大赛（M-CODE）参赛作品 · 基于麦当劳官方 MCP
> 知识截止 2026-10-14 联网核验；麦当劳 MCP 工具名已与官方 `M-China/mcd-mcp-server` 核对一致，入参/出参以运行时 MCP 返回为准。

## 一、项目介绍
点麦当劳时，优惠散落在官方 App 与美团等渠道，人工比价费时。本 Skill 让你**说一个单品名**，自动从「麦当劳官方 + 美团」两个渠道拉取当前可用优惠，按**到手价**比价排序，直接给出 Top3 最便宜拿法。

**核心能力**
- **双渠道聚合**：麦当劳官方 MCP（赛事指定，主力）+ 美团生活助手 Connector（增强渠道）。
- **单品筛选**：输入任意单品名，只留该单品的优惠（模糊匹配）。
- **比价排序**：归一化后按到手价升序，输出 Top3 + 省钱力度。

**技术栈**
- 数据层：麦当劳 MCP（streamablehttp）+ 美团生活助手（Connector，需连接）
- 逻辑层：`skills/mcd-deal-radar/scripts/aggregate.py`（Python 标准库，零依赖，可单测）
- 归一结构：`{channel, item, original, final, threshold, expires, how}`

## 二、目标用户
- 经常点麦当劳、想跨渠道比价省钱的普通用户
- 希望「一句话查单品优惠」的 WorkBuddy 用户
- 学习 MCP + Skill 开发的参赛新手（本包即可直接上架参考）

## 三、安装方法
1. **申请麦当劳 MCP Token**：访问 https://open.mcd.cn/mcp ，手机号登录 → 控制台 → 激活 → 复制 Token。
2. **在 WorkBuddy 接入麦当劳 MCP**（详见 `MCP_INTEGRATION.md`）：
   连接器 → 自定义连接器 → 配置 MCP，填入官方 JSON（`url=https://mcp.mcd.cn`，`type=streamablehttp`，`Authorization: Bearer <TOKEN>`）。
3. **安装本 Skill**：WorkBuddy → 专家 → 技能 → 上传技能，选择 `skills/mcd-deal-radar/`。
4. **（可选）连接美团生活助手** Connector 作为增强渠道（ connectors 中心搜索并 OAuth 授权）。

## 四、使用示例
```
用户：帮我查 麦辣鸡腿堡 现在官方和美团哪个便宜
Buddy：（调用麦当劳 MCP + 美团生活助手）→ 归一化 → 筛选「麦辣鸡腿堡」→ 比价
输出 Top3：
1. 美团 ¥13.9（满20，10-18 前，美团团购券）
2. 官方 ¥14.5（无门槛，10-20 前，麦当劳App领券）
3. 官方 ¥18.0（无门槛，10-15 前，会员日）
```

## 五、目录结构（参赛仓库根）
```
mcd-deal-radar/
├── README.md                     ★ 项目介绍/安装/示例/目标用户（官方必须）
├── CONTEST_DECLARATION.md        ★ 参赛声明（官方原版，内容不可改）
├── MCP_INTEGRATION.md            ★ 麦当劳 MCP 接入说明（官方必须）
├── workbuddy.md                  ★ WorkBuddy 开发上下文（3000 积分专项必须）
├── skills/mcd-deal-radar/        ★ 源代码（WorkBuddy Skill 包）
│   ├── SKILL.md
│   ├── references/               (麦当劳 MCP 工具清单 / 美团连接器 接入参考)
│   ├── scripts/aggregate.py      (归一化 + 单品筛选 + 比价排序，零依赖)
│   └── templates/query_prompt.md (单品筛选提问模板)
└── 使用与报名手册.md              (辅助文档：验证/安装/移动端/报名全链路)
```

## 六、合规与边界
- 所有 Token / 授权一律 `${VAR}` 占位，禁止硬编码明文。
- 优惠以各渠道实时返回为准，不编字段、不臆测力度；具体参数/返回结构以运行时 MCP 返回为准。
- 仅使用公开 / 授权接口，不爬登录后私有页。
- 麦当劳官方 MCP 为主心骨，美团为增强，避免偏离赛事主题。

## 七、报名与 3000 积分专项
1. 全程在 WorkBuddy 开发 → 导出对话 MD（见 `workbuddy.md`）。
2. 推 GitHub 公开仓库（含上述四个必须文件 + 源代码）。
3. 在 `M-China/mcd-developer-innovation-challenge` 用 Issue 模板提交「项目名称 + 项目地址 + 项目简介」即报名。
4. 进榜（Star>0）+ 前 100 + 提交 `workbuddy.md` → 获 WorkBuddy 3000 积分。

> 麦当劳 MCP 工具名已与官方 `M-China/mcd-mcp-server` 核对一致；各工具入参/出参以运行时返回为准，详见 `MCP_INTEGRATION.md` 第六节。
