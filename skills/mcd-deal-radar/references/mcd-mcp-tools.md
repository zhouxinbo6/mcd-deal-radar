# 麦当劳 MCP 工具清单（官方，已核对）

> 核对来源：官方仓库 `M-China/mcd-mcp-server` 的 README「# 3. 工具列表」
> 核对时间：2026-10-14（联网核验，default_branch = main）
> 接入：`https://mcp.mcd.cn`，Streamable HTTP，`Authorization: Bearer YOUR_MCP_TOKEN`
> 说明：官方 README 仅公布**工具名与用途**，**未公布每个工具的入参/出参 JSON Schema**；
> 实际参数与返回结构以运行时 MCP 返回为准（连接后在 WorkBuddy 中可见），请勿臆造字段。

## 本 Skill 实际调用的工具（已核对真实名）
| 用途 | 官方工具名 | 说明 |
|---|---|---|
| 单品菜单 | `query-meals` | 查询当前可售卖餐品列表（分类、餐品编码、标签），用于单品筛选 |
| 单品详情 | `query-meal-detail` | 按餐品编码查详情 / 套餐组成 |
| 当前可领优惠 | `available-coupons` | 麦麦省券列表（用户当前可领取的优惠券） |
| 门店可用券 | `query-store-coupons` | 当前门店下可用优惠券 |
| 活动日历 | `campaign-calendar` | 当月营销活动日历（进行中 / 往期 / 未来） |
| 到手价计算 | `calculate-price` | 计算订单价格，用于比价 / 到手价 |

## 全量官方工具（共 33 个，备查）
```
list-nutrition-foods, delivery-query-addresses, delivery-create-address, delivery-query-stores,
query-meal-assistance, query-nearby-stores, query-store-coupons, query-meals, query-meal-detail,
calculate-price, create-order, cancel-order, query-order, order-list, campaign-calendar,
available-coupons, auto-bind-coupons, query-my-coupons, query-my-account, mall-points-products,
mall-product-detail, mall-create-order, now-time-info, query-lottery-info, draw-lottery,
query-my-prizes, mall-order-list, mall-order-detail, query-party-city, query-party-store,
query-partystore-date, query-partystore-session, party-order-create
```

## 接入要点
- 鉴权：Bearer Token，本包统一用 `${MCD_MCP_TOKEN}` 占位，仅在 WorkBuddy 客户端配置。
- 协议：Streamable HTTP，由 WorkBuddy 连接器中心接入 `https://mcp.mcd.cn`。
- 地域：麦当劳优惠多为城市 / 门店级，`query-store-coupons` / `calculate-price` 需传入用户位置 / 门店参数（具体字段名以 MCP 运行时返回为准）。

## 参赛者注意
- 工具名已与官方仓库核对一致，**无需再替换占位名**。
- 仅各工具入参 / 出参 Schema 以运行时返回为准；`scripts/aggregate.py` 的 `normalize()` 字段按实际情况对齐即可。
- 美团生活助手（增强渠道）的真实 Tool 名仍待连接后核对，见 `references/meituan-connector.md`。
