# MCP 集成说明（MCP_INTEGRATION.md）

> 本文件说明「麦麦优惠雷达 Pro」实际使用的麦当劳 MCP Server、Tool、调用流程与业务价值。
> 知识截止 2026-10-14 联网核验（麦当劳 MCP 工具名已与官方 `M-China/mcd-mcp-server` 核对一致）；
> 各工具入参 / 出参 JSON Schema 以运行时 MCP 返回为准。

## 一、实际使用的麦当劳 MCP Server
- **Server**：麦当劳官方 MCP（赛事指定，本 Skill 主数据源）
- **接入地址**：`https://mcp.mcd.cn`
- **协议 / 类型**：`streamablehttp`
- **鉴权**：`Authorization: Bearer <TOKEN>`（Token 在 WorkBuddy 连接器配置，仓库内仅用占位符，不含明文）
- **官方使用指南**：https://github.com/M-China/mcd-mcp-server
- **活动仓库 / 规则**：https://github.com/M-China/mcd-developer-innovation-challenge

### WorkBuddy 侧配置 JSON（官方）
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_TOKEN"
      }
    }
  }
}
```
> 操作路径：WorkBuddy → 左侧【专家·技能·连接器】→【连接器】→ 右上角【自定义连接器】→【配置 MCP】→ 粘贴并保存 → 启用 `mcd-mcp`。

## 二、实际调用的 Tool（已核对官方真实名）
本 Skill 核心逻辑为「查优惠 → 单品筛选 → 比价」。麦当劳 MCP（mcp.mcd.cn）提供优惠 / 餐品 / 活动相关原子能力，本 Skill 实际调用：

- `available-coupons` —— 麦麦省券列表（用户当前可领优惠）
- `query-store-coupons` —— 当前门店下可用优惠券
- `campaign-calendar` —— 当月营销活动日历（活动型优惠）
- `query-meals` —— 当前可售卖餐品列表（单品筛选基础）
- `query-meal-detail` —— 餐品详情（套餐组成）
- `calculate-price` —— 计算到手价（比价核心）

> 工具名已与官方 `M-China/mcd-mcp-server` README「# 3. 工具列表」核对一致（2026-10-14）。
> 各工具的具体入参 / 出参 JSON Schema 官方 README 未列出，以运行时 MCP 返回为准。

## 三、调用流程
1. 用户说单品名（如「麦辣鸡腿堡」）。
2. WorkBuddy 调用麦当劳 MCP：优惠用 `available-coupons` / `query-store-coupons` / `campaign-calendar`，餐品用 `query-meals` / `query-meal-detail`，到手价用 `calculate-price`。
3. `scripts/aggregate.py` 的 `normalize()` 把返回拉平为统一结构 `{channel, item, original, final, threshold, expires, how}`。
4. `filter_by_item()` 模糊匹配，只留目标单品。
5. `rank()` 按 `final`（到手价）升序，`top_n()` 取 Top3 并算省钱力度。
6. 输出 Top3 清单（渠道 / 到手价 / 门槛 / 有效期 / 领法）。

**（可选增强）** 并行调用美团生活助手 Connector 查麦当劳团购券，一并归一化比价（美团 Connector 需在 WorkBuddy 连接器中心搜索并 OAuth 授权，当前账号默认未连接；其真实 Tool 名待连接后核对，见 `references/meituan-connector.md`）。

## 四、业务价值
- 把散落在多渠道的优惠集中比价，一句话拿到最便宜拿法。
- 基于官方实时数据，不编字段、不臆测力度。
- 可扩展：归一化结构预留 `channel` 字段，加新渠道只需补 `normalize()`。

## 五、本地联调（验证逻辑，无需 Token）
```bash
python skills/mcd-deal-radar/scripts/aggregate.py "麦辣鸡腿堡"
```
> 该脚本用内置样例验证归一化 / 筛选 / 排序逻辑，不依赖联网，便于提交前自检。

## 六、待确认事项（提交前核对）
- [ ] 各工具入参 / 出参 JSON Schema：以运行时 MCP 返回为准（官方 README 未列出）
- [ ] 地域（城市 / 门店）参数传入字段名：以 MCP 运行时返回为准
- [ ] 美团生活助手查询麦当劳券的真实 Tool 名（增强渠道，见 `references/meituan-connector.md`）
