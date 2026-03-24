from __future__ import annotations

from dataclasses import replace

from backend.app.schemas import FacilitySlot, OperatorRule, SchedulePlan, TeamAssignment


def _operator_base_score(op: OperatorRule, facility_type: str) -> float:
    return sum(s.effect_value for s in op.skills if s.facility_type == facility_type)


def _team_score(team: list[OperatorRule], facility_type: str) -> tuple[float, list[str]]:
    score = 0.0
    explanations: list[str] = []

    for op in team:
        base = _operator_base_score(op, facility_type)
        score += base
        if base > 0:
            explanations.append(f"{op.name_cn} 基础加成 +{base:.1f}")

    team_ids = {op.id for op in team}
    for op in team:
        for syn in op.synergies:
            if syn.facility_type != facility_type:
                continue
            if all(x in team_ids for x in syn.with_ops):
                score += syn.bonus
                explanations.append(f"{op.name_cn} 联动：{syn.description} +{syn.bonus:.1f}")

    return score, explanations


def _build_team(
    facility: FacilitySlot,
    available: dict[str, OperatorRule],
) -> tuple[list[OperatorRule], float, list[str]]:
    candidates = sorted(
        available.values(),
        key=lambda op: _operator_base_score(op, facility.facility_type),
        reverse=True,
    )

    team: list[OperatorRule] = []
    for op in candidates:
        if len(team) >= facility.slots:
            break
        if _operator_base_score(op, facility.facility_type) <= 0:
            continue
        team.append(op)

    score, explanations = _team_score(team, facility.facility_type)
    if not team:
        explanations = ["无匹配技能干员"]
    return team, score, explanations


def generate_schedule(
    owned_operator_ids: list[str],
    layout: list[FacilitySlot],
    rules: dict[str, OperatorRule],
) -> SchedulePlan:
    available = {op_id: rules[op_id] for op_id in owned_operator_ids if op_id in rules}
    assignments: list[TeamAssignment] = []

    for facility in layout:
        if not available:
            assignments.append(
                TeamAssignment(
                    facility_name=facility.name,
                    facility_type=facility.facility_type,
                    operators=[],
                    score=0,
                    explanations=["无可用干员"],
                )
            )
            continue

        team, score, explanations = _build_team(facility, available)

        assignments.append(
            TeamAssignment(
                facility_name=facility.name,
                facility_type=facility.facility_type,
                operators=[op.id for op in team],
                score=score,
                explanations=explanations,
            )
        )

        for op in team:
            available.pop(op.id, None)

    unassigned = sorted(available.keys())
    total = sum(a.score for a in assignments)
    return SchedulePlan(total_score=round(total, 2), assignments=assignments, unassigned_owned=unassigned)


def generate_alternative_plans(
    owned_operator_ids: list[str],
    layout: list[FacilitySlot],
    rules: dict[str, OperatorRule],
    top_k: int = 3,
) -> list[SchedulePlan]:
    baseline = generate_schedule(owned_operator_ids, layout, rules)
    plans = [baseline]

    removable = [op for op in owned_operator_ids if op in rules][: max(0, top_k - 1)]
    for op in removable:
        reduced = [x for x in owned_operator_ids if x != op]
        plan = generate_schedule(reduced, layout, rules)
        patched = replace(
            plan,
            total_score=round(plan.total_score * 0.98, 2),
        )
        plans.append(patched)

    plans.sort(key=lambda p: p.total_score, reverse=True)
    return plans[:top_k]
