#!/usr/bin/env python3
"""麦麦优惠雷达 Pro - 归一化 + 单品筛选 + 比价排序（零依赖，仅标准库）。

用法：
    python aggregate.py            # 跑内置示例
    python aggregate.py "麦辣鸡腿堡"   # 指定单品筛选并比价

数据由麦当劳 MCP + 美团生活助手 Connector 注入；本脚本只负责
「拉平结构 → 按单品筛选 → 按到手价比价 → 取 Top3」。
"""
from __future__ import annotations

import json
import sys
from typing import Iterable


def normalize(channel: str, item: str, original: float, final: float,
              threshold: str = "", expires: str = "", how: str = "") -> dict:
    """把任一渠道的优惠拉平成统一结构。"""
    return {
        "channel": channel,
        "item": item,
        "original": original,
        "final": final,
        "threshold": threshold,
        "expires": expires,
        "how": how,
    }


def filter_by_item(deals: Iterable[dict], keyword: str) -> list[dict]:
    """按单品名模糊匹配（包含即命中）。"""
    kw = (keyword or "").strip()
    if not kw:
        return list(deals)
    return [d for d in deals if kw in d.get("item", "")]


def savings_rate(d: dict) -> float:
    """省钱力度 = (原价 - 到手价) / 原价。"""
    if d["original"] <= 0:
        return 0.0
    return (d["original"] - d["final"]) / d["original"]


def rank(deals: Iterable[dict]) -> list[dict]:
    """按到手价升序。"""
    return sorted(deals, key=lambda d: d["final"])


def top_n(deals: Iterable[dict], n: int = 3) -> list[dict]:
    """取最便宜的 n 条，并附省钱力度标注。"""
    out = rank(deals)[:n]
    for d in out:
        d["省钱力度"] = f"{savings_rate(d) * 100:.1f}%"
    return out


def main() -> None:
    # 示例数据（实际由麦当劳 MCP + 美团生活助手注入）
    deals = [
        normalize("官方", "麦辣鸡腿堡", 21.0, 14.5, "无门槛", "2026-10-20", "麦当劳App领券"),
        normalize("美团", "麦辣鸡腿堡", 21.0, 13.9, "满20", "2026-10-18", "美团团购券"),
        normalize("官方", "麦辣鸡腿堡", 21.0, 18.0, "无门槛", "2026-10-15", "会员日"),
        normalize("美团", "巨无霸", 24.0, 19.9, "满24", "2026-10-19", "美团神券"),
    ]

    keyword = sys.argv[1] if len(sys.argv) > 1 else "麦辣鸡腿堡"
    matched = filter_by_item(deals, keyword)
    if not matched:
        print(f"未找到含「{keyword}」的优惠。")
        return
    result = top_n(matched, 3)
    print(f"「{keyword}」官方+美团 最便宜 Top3：")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
