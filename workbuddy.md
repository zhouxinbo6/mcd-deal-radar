# WorkBuddy 开发对话实录（workbuddy.md）

> 本文件为「麦麦优惠雷达 Pro（mcd-deal-radar）」项目在 **腾讯 WorkBuddy** 中的真实开发过程记录，
> 用于核验本项目是否「真实使用 WorkBuddy 开发」，以申请麦当劳程序员创意开发大赛 WorkBuddy 专项 3000 积分。
>
> - 开发者 GitHub：`zhouxinbo6`
> - 开发工具：腾讯 WorkBuddy（Ask / Plan / Craft 三模式 + 连接器 + 技能包）
> - 开发区间：2026-10-12 至 2026-10-14（北京时间）
> - 导出方式：由 WorkBuddy 会话导出整理

---

## 一、项目缘起（Ask 模式，2026-10-12）

用户提出需求：「帮我写一份 WorkBuddy 开发大神级新手教程，参考最新的 WorkBuddy 跟麦当劳的活动」。

WorkBuddy 侧动作：
1. 加载平台知识库技能，核验 WorkBuddy 平台能力（三模式、连接器、技能包上传）。
2. 联网检索并确认活动事实：**麦当劳 × WorkBuddy 程序员创意开发大赛（M-CODE）**，报名及排名期 2026-10-09 10:30 — 2026-10-25 23:59。
3. 输出《WorkBuddy 新手教程-MCODE实战.md》，含三模式心智模型、参赛流程、Skill 骨架、验收清单、提示词包。

## 二、确定选题（Plan 模式，2026-10-12）

用户诉求收敛：「我只想拿 3000 积分，拼不过」。

WorkBuddy 给出的策略：
- 澄清 3000 积分的真实规则（WorkBuddy 专项，需进前 100 名 + 真实使用 WorkBuddy + 提交 workbuddy.md）。
- 推荐「省事度」最高的方向：**麦麦今日优惠播报助手**（仅需调用麦当劳 MCP 查优惠工具）。
- 给出「硬性四件套」清单与 3 天时间盒。

## 三、需求升级为「麦麦优惠雷达 Pro」（Plan → Craft，2026-10-13）

用户提出：「能不能全网调最佳的优惠活动，含抖音、美团等，还可以按照想要的单品筛选优惠项」。

WorkBuddy 侧的处理（含边界澄清，反编造）：
1. 诚实拆解数据源边界：麦当劳 MCP 为赛事唯一官方结构化数据源；抖音无官方接口（放弃）；美团走生态内连接器。
2. 按用户指令「保留美团，去掉抖音」，确定最终架构为**双渠道**：麦当劳官方 MCP（主力）+ 美团生活助手 Connector（增强）。
3. 设计三层架构：采集层 → 归一化层 → 单品筛选 + 到手价比价层。

## 四、Skill 包实现（Craft 模式，2026-10-13）

WorkBuddy 在本机生成完整 Skill 包 `mcd-deal-radar/`：

```
skills/mcd-deal-radar/
├── SKILL.md                      # frontmatter 对齐官方规范（name/description/version/author）
├── references/
│   ├── mcd-mcp-tools.md          # 麦当劳 MCP 官方工具清单
│   └── meituan-connector.md      # 美团生活助手接入说明
├── scripts/aggregate.py          # 归一化 + 单品筛选 + 到手价排序（零依赖）
└── templates/query_prompt.md     # 单品筛选提问模板
```

关键实现：
- `aggregate.py` 提供 `normalize()` / `filter_by_item()` / `rank_and_top3()`：
  将各渠道优惠拉平为统一结构 `{渠道, 单品, 原价, 到手价, 门槛, 有效期, 领法}`，
  按单品名模糊匹配后，以到手价升序输出 Top3 与省钱力度。
- 冒烟测试：`python aggregate.py "麦辣鸡腿堡"` → 正常输出官方 + 美团 Top3 比价结果。

## 五、对齐官方报名要求（Craft 模式，2026-10-13 ~ 10-14）

WorkBuddy 侧动作：
1. 联网核验官方仓库与规则，纠正早期文档错误（三件套文件名 → 官方硬性命名）。
2. 生成官方命名的文件：`README.md` / `CONTEST_DECLARATION.md`（官方原版，一字不改）/ `MCP_INTEGRATION.md` / `mcp-config.example.json`。
3. 从官方 `M-China/mcd-mcp-server` 仓库提取全部 **33 个真实工具名**，将文档中的假设命名替换为官方名：
   - 查餐品 → `query-meals` / `query-meal-detail`
   - 查优惠 → `available-coupons` / `query-store-coupons`
   - 查活动 → `campaign-calendar`
   - 算到手价 → `calculate-price`
   并清除文档中的 `[INFO_GAP]` 工具名占位。
4. 生成 `mcp-deal-radar`（原文如此，即 mcd-deal-radar）GitHub 公开仓库并推送（`git init` → commit → push，仓库地址 https://github.com/zhouxinbo6/mcd-deal-radar ）。
5. 处理 git 网络受限问题：诊断 `github.com:443` 被阻断、`api.github.com` 可通，编写兜底上传脚本 `push_via_api.py`。
6. 清理误提交的 `__pycache__`，补充 `.gitignore`。

## 六、报名与反查（Craft 模式，2026-10-14）

1. 依据官方 README / `activityGuidelines.md` 的标准格式提交报名 Issue。
2. 首次提交（#678）因**正文格式未按标准模板**（缺首行 `【参赛申请】`、字段换行）被官方驳回。
3. WorkBuddy 反查官方规则原文，定位格式要求，输出修正版 Issue 文本（4 行固定格式），并整理为可直接复制的文件。

## 七、最终交付物

| 类别 | 文件 |
|---|---|
| 项目说明 | `README.md` |
| 参赛声明 | `CONTEST_DECLARATION.md`（官方原版，未改动） |
| MCP 集成说明 | `MCP_INTEGRATION.md` |
| MCP 配置示例 | `mcp-config.example.json`（仅环境变量占位符） |
| Skill 源码 | `skills/mcd-deal-radar/`（SKILL.md + references + scripts + templates） |
| WorkBuddy 开发凭证 | `workbuddy.md`（本文件） |

## 八、WorkBuddy 能力使用清单（对照「真实使用」核验）

- [x] 全程在 WorkBuddy 对话框中以自然语言交互完成需求分析、方案设计与代码生成
- [x] 使用 Ask 模式做事实核验与知识检索
- [x] 使用 Plan 模式收敛选题与架构
- [x] 使用 Craft 模式落地 Skill 包与 Git 仓库操作
- [x] 使用联网检索能力核验官方规则与工具清单
- [x] 使用终端能力在本机执行 Python 冒烟测试与 Git 提交

> 备注：本项目依赖的麦当劳 MCP 需在 WorkBuddy「连接器 → 自定义连接器 → 配置 MCP」中接入
> （`type: streamablehttp`，`url: https://mcp.mcd.cn`，`Authorization: Bearer <MCP_TOKEN>`），
> 配置示例见 `mcp-config.example.json`（脱敏）。
