from __future__ import annotations

import json
from pathlib import Path

from backend.app.schemas import FacilitySlot, OperatorRule, SkillEffect, SynergyRule

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "operator_skills_v1.json"


def load_operator_rules(path: Path = DATA_PATH) -> dict[str, OperatorRule]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    rules: dict[str, OperatorRule] = {}
    for item in raw["operators"]:
        rules[item["id"]] = OperatorRule(
            id=item["id"],
            name_cn=item["name_cn"],
            skills=[SkillEffect(**s) for s in item.get("skills", [])],
            synergies=[
                SynergyRule(
                    facility_type=s["facility_type"],
                    with_ops=s["with"],
                    bonus=s["bonus"],
                    description=s["description"],
                )
                for s in item.get("synergies", [])
            ],
        )
    return rules


LAYOUT_PRESETS: dict[str, list[FacilitySlot]] = {
    "252": [
        FacilitySlot("manufacture", 3, "制造站A"),
        FacilitySlot("manufacture", 3, "制造站B"),
        FacilitySlot("trade", 2, "贸易站A"),
        FacilitySlot("trade", 2, "贸易站B"),
        FacilitySlot("power", 1, "发电站"),
    ],
    "243": [
        FacilitySlot("manufacture", 3, "制造站A"),
        FacilitySlot("manufacture", 3, "制造站B"),
        FacilitySlot("trade", 2, "贸易站A"),
        FacilitySlot("trade", 2, "贸易站B"),
        FacilitySlot("power", 1, "发电站A"),
        FacilitySlot("power", 1, "发电站B"),
    ],
}
