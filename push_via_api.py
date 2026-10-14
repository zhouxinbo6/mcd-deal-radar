#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
push_via_api.py — GitHub Contents API 上传兜底脚本
=================================================
用途：当本机 `git push` 连不上 github.com:443（被网络/运营商阻断）时，
      改用「能通的 api.github.com」把整个目录逐文件上传 / 更新到 GitHub 仓库。
      本脚本零第三方依赖（仅用 Python 标准库），支持中文文件名。

先决条件：
  1) 一个 GitHub Personal Access Token（PAT），勾选 `repo` 权限。
     生成：GitHub → 右上角头像 → Settings → Developer settings →
           Personal access tokens → Tokens (classic) → Generate new token (classic) → 勾 repo
  2) token 只放在本机环境变量里，不要写进代码、不要发给我。

用法（Windows PowerShell）：
  cd "C:\\Users\\zhouxinbo\\WorkBuddy\\2026-10-12-16-54-25\\mcd-deal-radar"
  $env:GITHUB_TOKEN="ghp_你的token"
  python push_via_api.py

用法（Git Bash）：
  cd "/c/Users/zhouxinbo/WorkBuddy/2026-10-12-16-54-25/mcd-deal-radar"
  GITHUB_TOKEN=ghp_你的token python push_via_api.py

说明：
  - 已是同一内容会自动更新（先取 sha 再 PUT），可反复运行，幂等。
  - 默认跳过 .git 与脚本自身，避免把无关文件传上去。
  - 若哪个文件失败会打印 HTTP 状态与原因，逐条排查即可。
"""
import os
import sys
import json
import time
import base64
import urllib.request
import urllib.error
import urllib.parse

OWNER = "zhouxinbo6"
REPO = "mcd-deal-radar"
BRANCH = "main"
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
ROOT = os.path.dirname(os.path.abspath(__file__))
API = "https://api.github.com"

SKIP_DIRS = {".git", "__pycache__", ".idea", ".vscode"}
SKIP_FILES = {".DS_Store", "Thumbs.db", "push_via_api.py"}


def api(method, path, body=None):
    url = API + path
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "push-via-api")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8") or "{}"
            return r.status, json.loads(raw)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8") or "{}")
        except Exception:
            return e.code, {}
    except Exception as e:
        return 0, {"message": str(e)}


def get_sha(repo_path):
    p = "/repos/%s/%s/contents/%s?ref=%s" % (
        OWNER, REPO, urllib.parse.quote(repo_path), BRANCH)
    code, js = api("GET", p)
    if code == 200 and isinstance(js, dict):
        return js.get("sha")
    return None


def put_file(local_abs, repo_path):
    with open(local_abs, "rb") as f:
        content = base64.b64encode(f.read()).decode("ascii")
    sha = get_sha(repo_path)
    body = {
        "message": "chore: sync %s via Contents API" % repo_path,
        "content": content,
        "branch": BRANCH,
    }
    if sha:
        body["sha"] = sha
    p = "/repos/%s/%s/contents/%s" % (OWNER, REPO, urllib.parse.quote(repo_path))
    return api("PUT", p, body)


def main():
    if not TOKEN:
        print("ERROR: 未检测到环境变量 GITHUB_TOKEN。")
        print('PowerShell 示例: $env:GITHUB_TOKEN="ghp_xxx"; python push_via_api.py')
        sys.exit(1)

    code, js = api("GET", "/repos/%s/%s" % (OWNER, REPO))
    if code != 200:
        print("ERROR: 无法访问仓库 %s/%s (HTTP %s) -> %s" % (
            OWNER, REPO, code, js.get("message", "")))
        print("请确认：token 有效、勾了 repo 权限、仓库名正确。")
        sys.exit(1)

    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in SKIP_FILES:
                continue
            absp = os.path.join(dirpath, fn)
            rel = os.path.relpath(absp, ROOT).replace("\\", "/")
            files.append((absp, rel))

    print("待上传 %d 个文件 -> %s/%s@%s\n" % (len(files), OWNER, REPO, BRANCH))
    ok = fail = 0
    for absp, rel in sorted(files, key=lambda x: x[1]):
        c, j = put_file(absp, rel)
        if c in (200, 201):
            print("  OK   %s" % rel)
            ok += 1
        else:
            print("  FAIL %s  -> HTTP %s %s" % (rel, c, j.get("message", "")))
            fail += 1
        time.sleep(0.2)

    print("\n完成：成功 %d，失败 %d" % (ok, fail))
    print("仓库：https://github.com/%s/%s" % (OWNER, REPO))


if __name__ == "__main__":
    main()
