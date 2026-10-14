---
name: mcd-deal-radar
description: 基于麦当劳 MCP 与美团生活助手，按单品筛选并比价当前官方+美团渠道的最优麦当劳优惠。
description_zh: 麦麦优惠雷达 Pro：调用麦当劳 MCP 与美团生活助手，按单品筛选并比价官方+美团当前最优优惠。
description_en: McDonald's deal radar Pro - filter and compare McDonald's promos by item across official MCP and Meituan.
version: 1.0.0
author: zhouxinbo6
---

# 麦麦优惠雷达 Pro（mcd-deal-radar）

> 参赛作品 · 麦当劳 × WorkBuddy 程序员创意开发大赛（M-CODE）
> 知识截止 2026-09-07（平台结构）；M-CODE 信息 2026-10-12 联网核验；麦当劳 MCP 工具名 2026-10-14 已核对官方 `M-China/mcd-mcp-server`。

## 一句话定位
输入一个单品（如「麦辣鸡腿堡」），自动从 **麦当劳官方 MCP** + **美团生活助手** 两个渠道拉取当前可用优惠，归一化后按「到手价」比价排序，输出 Top3 最便宜拿法。

## 触发场景
- 「帮我查 麦辣鸡腿堡 现在在官方和美团上最便宜怎么拿」
- 「麦当劳 巨无霸 有什么优惠？按到手价排一下」
- 「我想凑单买 麦乐鸡，官方和美团哪个更划算」

## 数据源（双渠道，去掉抖音）
| 渠道 | 接口类型 | 状态 | 说明 |
|---|---|---|---|
| 麦当劳官方 | 麦当劳 MCP（赛事指定） | 必接 | 主力，结构化返回优惠/餐品/活动（官方接入 https://mcp.mcd.cn，streamablehttp，Bearer Token，见 MCP_INTEGRATION.md） |
| 美团 | 美团生活助手 Connector | 需先连接 | 查麦当劳团购券；你当前默认未连接，需授权 |

> 抖音已按需求移除。如需后续扩展，仅作为「待确认」接口位预留，不在本包内实现。

## 工作流程
1. **采集**：并行调用麦当劳 MCP（`available-coupons` / `query-store-coupons` / `campaign-calendar` 查优惠+活动；`query-meals` / `query-meal-detail` 查餐品；`calculate-price` 算到手价）与美团生活助手（查麦当劳团购券）。
2. **归一化**：用 `scripts/aggregate.py` 的 `normalize()` 把两渠道数据拉平成统一结构（见下）。
3. **单品筛选**：`filter_by_item(deals, 关键词)` 模糊匹配单品名，只留目标单品。
4. **比价排序**：`rank()` 按 `到手价` 升序，`top_n()` 取 Top3 并标注省钱力度。
5. **输出**：Top3 清单（渠道 / 到手价 / 门槛 / 有效期 / 领法）。

## 统一优惠结构
```json
{ "channel":"官方|美团", "item":"麦辣鸡腿堡", "original":21.0,
  "final":14.5, "threshold":"满20", "expires":"2026-10-20", "how":"App领券" }
```

## 边界与合规
- 所有密钥（麦当劳 MCP Token、美团授权）一律 `${VAR}` 占位，禁止硬编码。
- 优惠以各渠道实时返回为准，不编字段、不臆测力度；具体参数/返回结构以运行时 MCP 返回为准。
- 仅使用公开/授权接口，不爬登录后私有页。
- 麦当劳 MCP 必须为主心骨，美团为增强，避免被判「偏离赛事主题」。

## 调用示例
```
用户：帮我查 麦辣鸡腿堡 现在官方和美团哪个便宜
Buddy：调用麦当劳 MCP + 美团生活助手 → 归一化 → 筛选「麦辣鸡腿堡」→ 比价
输出 Top3：
1. 美团 ¥13.9（满20，10-18 前，美团团购券）
2. 官方 ¥14.5（无门槛，10-20 前，麦当劳App领券）
3. 官方 ¥18.0（无门槛，10-15 前，会员日）
```
