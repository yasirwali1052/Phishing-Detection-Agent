import json
from tools.traffic_analyzer import extract_features
from tools.dos_rules import is_ddos_attack
from tools.llm_explainer import llm_ddos_detector


def run_ddos_agent(file_path="data/sample_traffic.json"):
    with open(file_path, "r") as f:
        traffic_logs = json.load(f)

    print("\n🚨 DDoS Detection Agent (Rule + Groq LLM)")
    print("=" * 90)

    for i, log in enumerate(traffic_logs, 1):
        print(f"\n📦 Log #{i} — From IP: {log['src_ip']}")

        # Rule-based detection
        features = extract_features(log)
        rule_ddos, rule_reason = is_ddos_attack(features)

        # LLM-based detection (LangChain + Groq)
        llm_ddos, llm_reason = llm_ddos_detector(log)

        # Combined decision
        if rule_ddos or llm_ddos:
            print(" DDoS Detected")
            print(f" Rule-Based Reason: {rule_reason}")
            print(f" LLM-Based Reason: {llm_reason}")
        else:
            print(" Normal Traffic")
            print(f"Rule: {rule_reason}")
            print(f"LLM: {llm_reason}")

        print("-" * 90)


if __name__ == "__main__":
    run_ddos_agent()