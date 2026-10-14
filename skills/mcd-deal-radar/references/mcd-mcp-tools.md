# 麦当劳 MCP 工具清单（参考）

> 来源：麦当劳 × WorkBuddy M-CODE 大赛官方仓库 `McDonald's China (M-China)` → `mcd-developer-innovation-challenge`
> 知识截止 2026-10-12 联网核验。**以下工具名为本包假设命名，实际工具名 / 参数 / 返回结构以官方接入说明为准，标 `[INFO_GAP]` 处需参赛者核对官方文档后替换。**

## 假设可用的工具（待官方确认）
| 假设工具名 | 用途 | 返回（假设结构） |
|---|---|---|
| `mcd_promo_query` | 查当前优惠 | `[{item, original, final, threshold, expires, how}]` `[INFO_GAP]` |
| `mcd_menu_query` | 查餐品 | `[{item, price, category}]` `[INFO_GAP]` |
| `mcd_activity_query` | 查限时活动 | `[{name, item, rule, expires}]` `[INFO_GAP]` |

## 接入要点
- 鉴权：Bearer Token，本包统一用 `${MCD_MCP_TOKEN}` 占位。
- 协议：MCP（Model Context Protocol），由 WorkBuddy 连接器中心接入。
- 地域：麦当劳优惠多为城市/门店级，调用时需传入用户位置参数 `[INFO_GAP]`（以官方为准）。

## 参赛者待办
- [ ] 到 GitHub M-China 官方仓库核对上述工具的真实名称与参数
- [ ] 替换本包中所有 `[INFO_GAP]` 标记
- [ ] 将真实返回结构对齐 `scripts/aggregate.py` 的 `normalize()` 字段
