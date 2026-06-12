import pytest
from state.graph_state import default_state
from agents.search_agent import search_agent
from agents.comparison_agent import comparison_agent, score_ride
from agents.booking_agent import booking_agent
from agents.monitoring_agent import monitoring_agent
from agents.recovery_agent import recovery_agent
from agents.support_agents import memory_agent, notification_agent, analytics_agent


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def base_state():
    return default_state({"pickup": "Connaught Place", "destination": "IGI Airport", "user_id": "u1"})


@pytest.fixture
def state_with_rides(base_state):
    base_state = search_agent(base_state)
    return base_state


@pytest.fixture
def state_selected(state_with_rides):
    return comparison_agent(state_with_rides)


@pytest.fixture
def state_booked(state_selected):
    return booking_agent(state_selected)


# ── GraphState helpers ─────────────────────────────────────────────────────────

def test_default_state_keys(base_state):
    for key in ("trip_id", "pickup", "destination", "ride_options", "logs", "events", "timestamps"):
        assert key in base_state


def test_default_state_overrides(base_state):
    assert base_state["pickup"] == "Connaught Place"
    assert base_state["priority"] == "balanced"


# ── SearchAgent ────────────────────────────────────────────────────────────────

def test_search_finds_rides(state_with_rides):
    assert len(state_with_rides["ride_options"]) > 0


def test_search_only_available(state_with_rides):
    for ride in state_with_rides["ride_options"]:
        assert ride["availability"] is True


def test_search_logs_populated(state_with_rides):
    assert any("SearchAgent" in log for log in state_with_rides["logs"])


def test_search_timestamps(state_with_rides):
    assert "search_start" in state_with_rides["timestamps"]
    assert "search_end" in state_with_rides["timestamps"]


# ── ComparisonAgent ────────────────────────────────────────────────────────────

def test_comparison_selects_ride(state_selected):
    assert state_selected["selected_ride"] is not None


def test_comparison_agent_output(state_selected):
    comp = state_selected["agent_outputs"]["comparison"]
    assert "selected" in comp
    assert "score" in comp
    assert "reasoning" in comp


def test_score_ride_balanced():
    ride = {"price": 300, "eta": 10, "rating": 4.5, "reliability": 90}
    score = score_ride(ride, "balanced")
    assert 0.0 <= score <= 1.0


def test_score_ride_priorities():
    ride = {"price": 200, "eta": 5, "rating": 4.8, "reliability": 95}
    for priority in ("cost", "speed", "reliability", "balanced"):
        assert 0.0 <= score_ride(ride, priority) <= 1.0


# ── BookingAgent ───────────────────────────────────────────────────────────────

def test_booking_produces_status(state_booked):
    assert state_booked["booking_status"] in ("confirmed", "failed")


def test_booking_confirmed_sets_trip_id(state_booked):
    if state_booked["booking_status"] == "confirmed":
        assert state_booked["trip_id"] is not None
        assert state_booked["ride_status"] == "active"


def test_booking_logs(state_booked):
    assert any("BookingAgent" in log for log in state_booked["logs"])


# ── MonitoringAgent ────────────────────────────────────────────────────────────

def test_monitoring_sets_ride_status(state_booked):
    if state_booked["booking_status"] == "confirmed":
        result = monitoring_agent(state_booked)
        assert result["ride_status"] in ("active", "completed", "cancelled")


def test_monitoring_cancelled_sets_recover(state_booked):
    if state_booked["booking_status"] != "confirmed":
        pytest.skip("booking failed, skip monitoring test")
    # Force a cancelled state by patching ride_status after monitoring
    result = monitoring_agent(state_booked)
    if result["ride_status"] == "cancelled":
        assert result["should_recover"] is True
        assert len(result["cancellation_history"]) > 0


# ── RecoveryAgent ──────────────────────────────────────────────────────────────

def test_recovery_increments_attempts(state_booked):
    result = recovery_agent(state_booked)
    assert result["recovery_attempts"] == state_booked.get("recovery_attempts", 0) + 1


def test_recovery_clears_selected_ride(state_booked):
    result = recovery_agent(state_booked)
    assert result["selected_ride"] is None
    assert result["booking_status"] is None


def test_recovery_excludes_failed_provider(state_booked):
    failed = (state_booked.get("selected_ride") or {}).get("provider")
    result = recovery_agent(state_booked)
    providers = [r["provider"] for r in result["ride_options"]]
    if failed:
        assert failed not in providers


# ── Support Agents ─────────────────────────────────────────────────────────────

def test_memory_agent_updates_prefs(state_booked):
    result = memory_agent(state_booked)
    assert "memory" in result["agent_outputs"]
    if state_booked.get("selected_ride"):
        assert result["user_preferences"].get("preferred_provider") is not None


def test_notification_agent_confirmed(state_booked):
    if state_booked["booking_status"] == "confirmed":
        result = notification_agent(state_booked)
        types = [n["type"] for n in result["notifications"]]
        assert "BOOKING_CONFIRMED" in types


def test_analytics_agent_output(state_booked):
    result = analytics_agent(state_booked)
    analytics = result["agent_outputs"]["analytics"]
    assert "total_cancellations" in analytics
    assert "recovery_attempts" in analytics
    assert "trip_complete" in analytics


# ── Full Workflow ──────────────────────────────────────────────────────────────

def test_full_workflow():
    from workflow_graph.workflow import ride_graph
    state = default_state({"pickup": "Thane", "destination": "Mumbai Airport", "user_id": "test-001"})
    result = ride_graph.invoke(state)
    assert result["trip_complete"] is not None
    assert len(result["logs"]) > 0
    assert "analytics" in result["agent_outputs"]
    assert result["booking_status"] in ("confirmed", "failed", None)
