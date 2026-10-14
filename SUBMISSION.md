# 报名提交指引（zhouxinbo6）

> 本文件是「你登录后」要执行的最后几步。

---

## 〇、⚠️ 报名失败反查结论（issue #678）

**失败通知**：`您的作品未通过审核，失败原因：您的报名信息未通过校验。您可以检查issue格式是否符合标准格式，并重新issue。`

**根因**：Issue 正文未按官方「标准格式」撰写。官方 README / `activityGuidelines.md` 给出的唯一标准格式是**固定 4 行、首行固定文案 `【参赛申请】`**：

```text
【参赛申请】
项目名称：麦当劳营养膳食专家
项目地址：https://github.com/M-China/skills
项目简介：身材管控期也想吃麦当劳？这个专家会帮你根据每日消耗搭配麦麦套餐
```

**#678 实际提交内容的问题**：

| # | 问题 | 说明 |
|:--:|---|---|
| 1 | **缺 `【参赛申请】` 首行** | 这是格式校验器的锚点，缺失直接判不合格 |
| 2 | `项目简介` 被写成 `简介：` 并**另起一行** | 官方明确警告「【项目简介】和项目简介内容之间暂不要使用换行符」 |
| 3 | 多了 `开发者：zhouxinbo6` 一行 | 非模板字段，多余行会干扰严格校验 |
| 4 | 正文含空行 + 编号列表 + 多条换行 | 官方警告「报名 Issue 的标题和正文之间暂不要使用换行符」 |

**注意：这与仓库内容无关。** 你的仓库文件本身是齐的（五件套 + 源码），只需**按标准格式重新提一个 Issue**即可。

---

## 一、重新提交 Issue（唯一必做，修正版）

打开 https://github.com/M-China/mcd-developer-innovation-challenge → **Issues → New issue**

### ① Add a title（标题栏）
```
麦麦优惠雷达 Pro（mcd-deal-radar）
```

### ② Add a description（正文框，整段粘贴，4 行、无空行）
```
【参赛申请】
项目名称：麦麦优惠雷达 Pro（mcd-deal-radar）
项目地址：https://github.com/zhouxinbo6/mcd-deal-radar
项目简介：基于麦当劳官方 MCP 开发的优惠雷达 Skill，可按单品筛选优惠并按到手价排序输出最优拿法，全程使用 WorkBuddy 完成开发
```

### ③ 提交
右侧 Assignees / Labels / Projects / Milestone **全部不动**，`Create more` **不勾** → 点绿色 **Create**。

> **三条硬规矩（务必遵守）**：
> 1. 正文**第 1 行必须是** `【参赛申请】`，前面不能有空行；
> 2. 四个字段**各占一行**，字段名与内容之间**不能换行**；
> 3. 项目地址**必须是纯文本 URL**，**不要**用 `[文字](链接)` 的 Markdown 形式。

> 旧的 #678 可以不用管（已判失败），若想干净可点 **Close issue** 关掉它；重要的是**新建**一个合规 Issue。

---

## 二、仓库文件自查（报名条件项）

| 文件 | 官方要求 | 状态 |
|---|---|---|
| `README.md` | 必须，文件名不可改 | ✅ |
| `CONTEST_DECLARATION.md` | 必须，**文件名与内容均不可改** | ✅ 官方原版 |
| `MCP_INTEGRATION.md` | 必须，文件名不可改 | ✅ |
| `mcp-config.example.json` | 必须，脱敏、仅允许环境变量占位 | ✅ |
| 源代码 | 必须 | ✅ `skills/mcd-deal-radar/` |
| `workbuddy.md` | WorkBuddy 专项 3000 分必备，文件名不可改 | ✅ 已替换为真实开发实录 |

> 报名条件另要求：仓库为 **Public**（已是）；项目创建时间在 **2025-12-25 ~ 2026-10-25** 之间（你的仓库创建于 2026-10-14，符合）。

---

## 三、3000 积分的真实门槛（诚实版）

官方奖励原文：
- 排行榜**前 100 名**（Star > 0 才进榜）中，**真实使用 WorkBuddy 且提交了 `workbuddy.md`** 的项目 → **每人 3000 积分**。
- 前 3 名：无论是否用 WorkBuddy，各得 10240 积分。

**推论**：想拿 3000 分，必须满足 ①报名成功（本文件第一节）②`workbuddy.md` 为真实开发凭证 ③至少 1 个 Star 进榜。

---

## 四、推送（沙箱网络受限时的兜底）

若 `git push` 报 `Failed to connect to github.com:443`，属本机网络阻断。可选：
- **换网络**重试（历史上有成功记录）；
- **配代理**：`git config --global http.proxy http://127.0.0.1:端口`（推完 `--unset`）；
- **走 api.github.com 兜底**（脚本 `push_via_api.py`）：生成 PAT 后
  ```powershell
  cd "C:\Users\zhouxinbo\WorkBuddy\2026-10-12-16-54-25\mcd-deal-radar"
  $env:GITHUB_TOKEN="ghp_你的token"
  python push_via_api.py
  ```

## 五、Win 下提交（本地已 commit，只差 push）
```bash
cd "C:\Users\zhouxinbo\WorkBuddy\2026-10-12-16-54-25\mcd-deal-radar"
git push
```
