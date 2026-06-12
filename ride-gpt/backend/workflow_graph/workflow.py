from langgraph.graph import StateGraph, END
from state.graph_state import GraphState
from agents.search_agent import search_agent
from agents.comparison_agent import comparison_agent
from agents.booking_agent import booking_agent
from agents.monitoring_agent import monitoring_agent
from agents.recovery_agent import recovery_agent
from agents.support_agents import memory_agent, notification_agent, analytics_agent


def route_after_monitoring(state: dict) -> str:
    if state.get("trip_complete"):
        return "analytics"
    if state.get("should_recover") and state.get("recovery_attempts", 0) < 3:
        return "recovery"
    return "analytics"


def route_after_booking(state: dict) -> str:
    return "recovery" if state.get("booking_status") == "failed" else "monitoring"


def route_after_recovery(state: dict) -> str:
    return "analytics" if state.get("trip_complete") or state.get("error") else "search"


def build_graph() -> StateGraph:
    graph = StateGraph(GraphState)

    graph.add_node("search", search_agent)
    graph.add_node("comparison", comparison_agent)
    graph.add_node("booking", booking_agent)
    graph.add_node("monitoring", monitoring_agent)
    graph.add_node("recovery", recovery_agent)
    graph.add_node("memory", memory_agent)
    graph.add_node("notification", notification_agent)
    graph.add_node("analytics", analytics_agent)

    graph.set_entry_point("search")
    graph.add_edge("search", "comparison")
    graph.add_edge("comparison", "booking")
    graph.add_conditional_edges("booking", route_after_booking, {"monitoring": "monitoring", "recovery": "recovery"})
    graph.add_conditional_edges("monitoring", route_after_monitoring, {"analytics": "analytics", "recovery": "recovery"})
    graph.add_conditional_edges("recovery", route_after_recovery, {"search": "search", "analytics": "analytics"})
    graph.add_edge("analytics", "memory")
    graph.add_edge("memory", "notification")
    graph.add_edge("notification", END)

    return graph.compile()


ride_graph = build_graph()
