from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

FacilityType = Literal["manufacture", "trade", "power", "control", "dorm"]


@dataclass(frozen=True)
class SkillEffect:
    facility_type: FacilityType
    effect_type: str
    effect_value: float
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class SynergyRule:
    facility_type: FacilityType
    with_ops: list[str]
    bonus: float
    description: str


@dataclass(frozen=True)
class OperatorRule:
    id: str
    name_cn: str
    skills: list[SkillEffect]
    synergies: list[SynergyRule]


@dataclass(frozen=True)
class FacilitySlot:
    facility_type: FacilityType
    slots: int
    name: str


@dataclass(frozen=True)
class TeamAssignment:
    facility_name: str
    facility_type: FacilityType
    operators: list[str]
    score: float
    explanations: list[str]


@dataclass(frozen=True)
class SchedulePlan:
    total_score: float
    assignments: list[TeamAssignment]
    unassigned_owned: list[str]
