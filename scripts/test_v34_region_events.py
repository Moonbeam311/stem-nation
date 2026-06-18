from copy import deepcopy

BASE_METRICS = {
    "food": 50,
    "stability": 50,
    "knowledge": 50,
    "unity": 50,
    "territory": 50,
    "wealth": 50,
}

EXPECTED = {
    "river corridor": {
        "event": "RIVER_FLOOD_RISK_EVENT",
        "alert": "RIVER_FLOOD_ALERT",
        "metrics": {"food": 55, "stability": 45, "knowledge": 50, "unity": 50, "territory": 50, "wealth": 50},
    },
    "forest belt": {
        "event": "FOREST_RESOURCE_EVENT",
        "alert": "FOREST_WILDFIRE_ALERT",
        "metrics": {"food": 50, "stability": 45, "knowledge": 55, "unity": 50, "territory": 50, "wealth": 55},
    },
    "mountain ridge": {
        "event": "MOUNTAIN_DEFENSE_EVENT",
        "alert": "MOUNTAIN_WINTER_ALERT",
        "metrics": {"food": 45, "stability": 55, "knowledge": 50, "unity": 50, "territory": 55, "wealth": 50},
    },
    "desert basin": {
        "event": "DESERT_SCARCITY_EVENT",
        "alert": "DESERT_SURVIVAL_ALERT",
        "metrics": {"food": 45, "stability": 45, "knowledge": 50, "unity": 50, "territory": 50, "wealth": 55},
    },
    "coastal exchange": {
        "event": "COASTAL_TRADE_EVENT",
        "alert": "COASTAL_STORM_ALERT",
        "metrics": {"food": 50, "stability": 45, "knowledge": 50, "unity": 50, "territory": 55, "wealth": 55},
    },
    "balanced valley": {
        "event": "BALANCED_GROWTH_EVENT",
        "alert": "BALANCED_FOUNDATION_ALERT",
        "metrics": {"food": 53, "stability": 53, "knowledge": 50, "unity": 53, "territory": 50, "wealth": 50},
    },
}

def apply_region_engine(region: str):
    region_key = region.lower()
    metrics = deepcopy(BASE_METRICS)
    events = []
    alerts = []

    if "river" in region_key:
        events.append("RIVER_FLOOD_RISK_EVENT")
        alerts.append("RIVER_FLOOD_ALERT")
        metrics["food"] += 5
        metrics["stability"] -= 5

    if "forest" in region_key:
        events.append("FOREST_RESOURCE_EVENT")
        alerts.append("FOREST_WILDFIRE_ALERT")
        metrics["wealth"] += 5
        metrics["knowledge"] += 5
        metrics["stability"] -= 5

    if "mountain" in region_key:
        events.append("MOUNTAIN_DEFENSE_EVENT")
        alerts.append("MOUNTAIN_WINTER_ALERT")
        metrics["territory"] += 5
        metrics["stability"] += 5
        metrics["food"] -= 5

    if "desert" in region_key:
        events.append("DESERT_SCARCITY_EVENT")
        alerts.append("DESERT_SURVIVAL_ALERT")
        metrics["food"] -= 5
        metrics["stability"] -= 5
        metrics["wealth"] += 5

    if "coastal" in region_key:
        events.append("COASTAL_TRADE_EVENT")
        alerts.append("COASTAL_STORM_ALERT")
        metrics["wealth"] += 5
        metrics["territory"] += 5
        metrics["stability"] -= 5

    if "balanced" in region_key or "valley" in region_key:
        events.append("BALANCED_GROWTH_EVENT")
        alerts.append("BALANCED_FOUNDATION_ALERT")
        metrics["food"] += 3
        metrics["stability"] += 3
        metrics["unity"] += 3

    return {
        "metrics": metrics,
        "events": events,
        "alerts": alerts,
    }

def main():
    failures = []

    for region, expected in EXPECTED.items():
        result = apply_region_engine(region)

        event_ok = expected["event"] in result["events"]
        alert_ok = expected["alert"] in result["alerts"]
        metrics_ok = result["metrics"] == expected["metrics"]

        status = "PASS" if event_ok and alert_ok and metrics_ok else "FAIL"
        print(f"{status}: {region}")

        if not event_ok:
            failures.append(f"{region}: missing event {expected['event']}")
        if not alert_ok:
            failures.append(f"{region}: missing alert {expected['alert']}")
        if not metrics_ok:
            failures.append(f"{region}: metrics expected {expected['metrics']} got {result['metrics']}")

    if failures:
        print("\nFAILURES:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("\nAll V34 region event tests passed.")

if __name__ == "__main__":
    main()
