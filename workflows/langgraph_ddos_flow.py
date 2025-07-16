from langgraph.graph import StateGraph, END
from tools.traffic_analyzer import extract_features
from tools.ddos_rules import is_ddos_attack
from tools.llm_explainer import llm_ddos_detector

def ddos_node(state):
    log = state.get("log")
    features = extract_features(log)
    rule_ddos, rule_reason = is_ddos_attack(features)
    llm_ddos, llm_reason = llm_ddos_detector(log)

    state["result"] = {
        "is_ddos": rule_ddos or llm_ddos,
        "rule_reason": rule_reason,
        "llm_reason": llm_reason
    }

    return state

def build_ddos_graph():
    builder = StateGraph()
    builder.add_node("ddos_node", ddos_node)
    builder.set_entry_point("ddos_node")
    builder.add_edge("ddos_node", END)
    return builder.compile()

if __name__ == "__main__":
    import json
    with open("data/sample_traffic.json", "r") as f:
        logs = json.load(f)

    graph = build_ddos_graph()

    for log in logs:
        state = {"log": log}
        result = graph.invoke(state)
        print("🧪 Log Result:", result["result"])
        print("=" * 60)