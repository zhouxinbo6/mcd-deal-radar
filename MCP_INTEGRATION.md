# MCP 集成说明（MCP_INTEGRATION.md）

> 本文件说明「麦麦优惠雷达 Pro」实际使用的麦当劳 MCP Server、Tool、调用流程与业务价值。
> 知识截止 2026-10-12 联网核验；具体 Tool 名 / 参数 / 返回结构以官方仓库 `M-China/mcd-mcp-server` 与 `M-China/mcd-developer-innovation-challenge` 为准。

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

## 二、实际调用的 Tool
本 Skill 核心逻辑为「查优惠 → 单品筛选 → 比价」。麦当劳 MCP 提供优惠 / 餐品 / 活动相关原子能力。
具体 Tool 名称与参数以官方 `mcd-mcp-server` 仓库为准；本仓库 `skills/mcd-deal-radar/references/mcd-mcp-tools.md` 列出假设命名与待核对清单（标 `[INFO_GAP]`）。

**调用计划（按能力映射）**
- 查当前优惠（如 `promo_query`）→ 取单品级优惠
- 查餐品（如 `menu_query`）→ 补全单品名 / 价格
- 查限时活动（如 `activity_query`）→ 补充活动型优惠

## 三、调用流程
1. 用户说单品名（如「麦辣鸡腿堡」）。
2. WorkBuddy 调用麦当劳 MCP 相关 Tool 拉取当前优惠 / 餐品 / 活动。
3. `scripts/aggregate.py` 的 `normalize()` 把返回拉平为统一结构 `{channel, item, original, final, threshold, expires, how}`。
4. `filter_by_item()` 模糊匹配，只留目标单品。
5. `rank()` 按 `final`（到手价）升序，`top_n()` 取 Top3 并算省钱力度。
6. 输出 Top3 清单（渠道 / 到手价 / 门槛 / 有效期 / 领法）。

**（可选增强）** 并行调用美团生活助手 Connector 查麦当劳团购券，一并归一化比价（美团 Connector 需在 WorkBuddy 连接器中心搜索并 OAuth 授权，当前账号默认未连接）。

## 四、业务价值
- 把散落在多渠道的优惠集中比价，一句话拿到最便宜拿法。
- 基于官方实时数据，不编字段、不臆测力度。
- 可扩展：归一化结构预留 `channel` 字段，加新渠道只需补 `normalize()`。

## 五、本地联调（验证逻辑，无需 Token）
```bash
python skills/mcd-deal-radar/scripts/aggregate.py "麦辣鸡腿堡"
```
> 该脚本用内置样例验证归一化 / 筛选 / 排序逻辑，不依赖联网，便于提交前自检。

## 六、待官方确认字段清单（提交前必核，禁止占位参赛）
- [ ] 麦当劳 MCP 真实 Tool 名 / 参数 / 返回结构（核对 `mcd-mcp-server`）
- [ ] 地域（城市 / 门店）参数传入方式
- [ ] 美团生活助手查询麦当劳券的真实 Tool 名（如启用增强渠道）
- [ ] 两渠道优惠时效性字段命名

> 凡标 `[INFO_GAP]` 处，均需在提交前对照官方文档替换后再参赛。
