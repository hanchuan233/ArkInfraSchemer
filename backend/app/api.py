from __future__ import annotations

from dataclasses import asdict

from backend.app.services.rules import LAYOUT_PRESETS, load_operator_rules
from backend.app.services.scheduler import generate_alternative_plans


def parse_roster_from_manual(names_or_ids: list[str]) -> dict:
    """V1 临时接口：手动输入干员 ID，模拟截图识别后的结果。"""
    rules = load_operator_rules()
    normalized = [name.strip().lower() for name in names_or_ids]
    owned = [op_id for op_id in normalized if op_id in rules]
    unresolved = [op_id for op_id in normalized if op_id not in rules]
    return {
        "operators": owned,
        "unresolved": unresolved,
        "source": "manual-input-v1",
    }


def generate_schedule_api(payload: dict) -> dict:
    rules = load_operator_rules()
    layout_key = payload.get("layout", "252")
    top_k = int(payload.get("top_k", 3))
    owned = payload.get("owned_operator_ids", [])

    if layout_key not in LAYOUT_PRESETS:
        raise ValueError(f"unsupported layout: {layout_key}")

    plans = generate_alternative_plans(
        owned_operator_ids=owned,
        layout=LAYOUT_PRESETS[layout_key],
        rules=rules,
        top_k=top_k,
    )
    return {
        "layout": layout_key,
        "top_k": top_k,
        "plans": [asdict(p) for p in plans],
    }
