# 报名提交指引（zhouxinbo6）

> 本文件是「你登录后」要执行的最后几步。仓库已 `git init` + 首次提交，只差推送和报名。

## 一、推送代码到 GitHub（需你本人登录授权）

方式 A（推荐，用 GitHub CLI，首次会弹浏览器登录）：
```bash
# 1) 打开终端，进入本目录
cd "C:\Users\zhouxinbo\WorkBuddy\2026-10-12-16-54-25\mcd-deal-radar"

# 2) 登录 GitHub（浏览器弹窗，用 zhouxinbo6 账号授权）
gh auth login

# 3) 创建公开仓库并推送（一行搞定）
gh repo create mcd-deal-radar --public --source=. --push
```
方式 B（手动）：先在 github.com 新建公开仓库 `mcd-deal-radar`，再：
```bash
git remote add origin https://github.com/zhouxinbo6/mcd-deal-radar.git
git branch -M main
git push -u origin main
```
> 推送时若提示输入账号密码：用户名填 `zhouxinbo6`，密码填 **GitHub Personal Access Token**（不是登录密码；在 github.com → Settings → Developer settings → PAT 生成，勾 repo 权限）。

## 二、提交参赛 Issue（M-China 官方仓库）

打开 https://github.com/M-China/mcd-developer-innovation-challenge ，用 **Issue 模板**提交，内容直接复制下面：

```
标题：M-CODE 参赛：麦麦优惠雷达 Pro（mcd-deal-radar）

项目名称：麦麦优惠雷达 Pro（mcd-deal-radar）
项目地址：https://github.com/zhouxinbo6/mcd-deal-radar
开发者：zhouxinbo6

简介：
基于麦当劳官方 MCP（mcp.mcd.cn）+ 美团生活助手连接器，按单品筛选并比价
官方与美团渠道当前最优麦当劳优惠的 Skill。核心能力：
1. 单品级优惠筛选（如「麦辣鸡腿堡」）；
2. 双渠道归一化比价，按到手价升序输出 Top3 + 省钱力度；
3. 全程使用 WorkBuddy 开发（对话上下文已导出 workbuddy.md）。
已提交官方四件套（README / CONTEST_DECLARATION / MCP_INTEGRATION / workbuddy）+ Skill 源码。
```

## 三、CSDN builderx 活动页（你给的链接）

地址：`https://builderx.csdn.net/activity-site/m-code/pages?sessionid=`（sessionid 需你登录后补全）

我无法替你登录或填该页。登录后，页面通常要求：
1. 绑定 GitHub 账号（授权）；
2. 粘贴仓库地址 `https://github.com/zhouxinbo6/mcd-deal-radar`；
3. 点「提交/报名」。

登录后把页面截图或贴出字段名发我，我逐步教你点。

## 四、报名前必做（否则判占位）
- [ ] 麦当劳 MCP 工具名已核对官方 `mcd-mcp-server`（无需再替换）；各工具入参/出参以运行时返回为准；美团 Tool 名待连接后核对
- [ ] 确认麦当劳 MCP 已在 WorkBuddy 连接并真调通
- [ ] 公开仓库含四件套 + Skill 源码
- [ ] 导出开发对话 MD 已入库（workbuddy.md）
