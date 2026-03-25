from backend.app.api import generate_schedule_api, parse_roster_from_manual


def test_parse_roster_from_manual_splits_unresolved() -> None:
    result = parse_roster_from_manual(["texas", "unknown", "exusiai"])
    assert result["operators"] == ["texas", "exusiai"]
    assert result["unresolved"] == ["unknown"]


def test_generate_schedule_api_returns_ranked_plans() -> None:
    payload = {
        "layout": "252",
        "top_k": 2,
        "owned_operator_ids": ["texas", "lappland", "exusiai", "saria", "ptilopsis", "courier"],
    }

    result = generate_schedule_api(payload)

    assert result["layout"] == "252"
    assert len(result["plans"]) == 2
    assert result["plans"][0]["total_score"] >= result["plans"][1]["total_score"]
    assignments = result["plans"][0]["assignments"]
    assert any(a["facility_type"] == "trade" for a in assignments)
    assert any(a["facility_type"] == "manufacture" for a in assignments)
