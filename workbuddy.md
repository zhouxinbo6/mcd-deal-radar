# WorkBuddy 开发上下文（workbuddy.md）

> 本文件用于核验本项目是否「使用 WorkBuddy 真实开发」，以申请 WorkBuddy 专项 3000 积分。
> 提交要求：使用 WorkBuddy 开发 Skill 时的对话上下文（可导出为 MD）。文件名不可改动。

## 一、本项目与 WorkBuddy 的关系
- 「麦麦优惠雷达 Pro」全程在 WorkBuddy 中构思、开发与调试。
- 使用 WorkBuddy 的 Ask / Plan / Craft 三模式，结合连接器（麦当劳 MCP / 美团生活助手）与 Skill 上传能力完成。
- 用户在 WorkBuddy 对话框中以自然语言直接触发本 Skill（如「帮我查 麦辣鸡腿堡 官方和美团哪个便宜」）。

## 二、对话上下文导出指引（参赛者自操作）
1. 在 WorkBuddy 中打开开发本项目的完整对话。
2. 使用 WorkBuddy 的「导出对话」功能，将对话保存为 Markdown。
3. 将导出的真实对话 MD 内容补充 / 替换到本文件（保持文件名 `workbuddy.md`），随仓库一起提交。

## 三、核验要点（对应 3000 积分条件）
- 项目进入排行榜（Star > 0）且排名前 100。
- 真实使用 WorkBuddy 开发（本文件 + 对话导出为证）。
- 提交 `workbuddy.md`（本文件）。
- 仓库为公开仓库，且含 `README.md` / `CONTEST_DECLARATION.md` / `MCP_INTEGRATION.md` / 源代码。

## 四、MCP 接入（WorkBuddy 侧）
- 麦当劳 MCP：连接器 → 自定义连接器 → 配置 MCP（见 `MCP_INTEGRATION.md`，官方 `url=https://mcp.mcd.cn`，`streamablehttp`，Bearer Token）。
- 美团生活助手：连接器中心搜索并 OAuth 授权（增强渠道，可选）。

## 五、开发时间线（参赛项目创建时间须在 2025-12-25 至 2026-10-25 之间）
- 本仓库创建 / 首次提交时间：____（参赛者填写，须落在上述窗口内）
- WorkBuddy 开发对话区间：____（参赛者填写，建议与仓库提交时间一致）

> 注：本文件为模板。正式参赛时，请将「导出对话 MD」的真实内容补充至此，确保能证明真实的 WorkBuddy 开发过程；仓库创建时间务必落在官方允许窗口内。
