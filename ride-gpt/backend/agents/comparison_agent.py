from state.graph_state import add_log, set_timestamp


def score_ride(ride: dict, priority: str) -> float:
    weights = {
        "cost":        {"reliability": 0.20, "price": 0.50, "eta": 0.20, "rating": 0.10},
        "speed":       {"reliability": 0.20, "price": 0.10, "eta": 0.60, "rating": 0.10},
        "reliability": {"reliability": 0.60, "price": 0.10, "eta": 0.20, "rating": 0.10},
        "balanced":    {"reliability": 0.40, "price": 0.30, "eta": 0.20, "rating": 0.10},
    }
    w = weights.get(priority, weights["balanced"])
    price_score = max(0, (500 - ride["price"]) / 500)
    eta_score = max(0, (30 - ride["eta"]) / 30)
    reliability_score = ride["reliability"] / 100
    rating_score = (ride["rating"] - 1) / 4
    return round(
        w["reliability"] * reliability_score +
        w["price"] * price_score +
        w["eta"] * eta_score +
        w["rating"] * rating_score,
        4,
    )


def comparison_agent(state: dict) -> dict:
    state = set_timestamp(state, "comparison_start")
    state = add_log(state, "ComparisonAgent", "Ranking available rides")

    ride_options = state.get("ride_options", [])
    priority = state.get("priority", "balanced")

    valid = [r for r in ride_options if r["rating"] >= 4.0 and r["eta"] <= 25 and r["reliability"] >= 70]
    if not valid:
        valid = ride_options
        state = add_log(state, "ComparisonAgent", "No rides passed quality filter; using all options")

    scored = sorted(valid, key=lambda r: score_ride(r, priority), reverse=True)
    best = scored[0]
    best_score = score_ride(best, priority)

    agent_outputs = dict(state.get("agent_outputs", {}))
    agent_outputs["comparison"] = {
        "selected": best,
        "score": best_score,
        "reasoning": f"Selected {best['provider']} — price ₹{best['price']}, ETA {best['eta']}min, reliability {best['reliability']:.1f}%, rating {best['rating']}",
        "alternatives": scored[1:],
    }
    state = {**state, "selected_ride": best, "agent_outputs": agent_outputs}
    state = add_log(state, "ComparisonAgent", f"Selected {best['provider']} with score {best_score}")
    state = set_timestamp(state, "comparison_end")
    return state
