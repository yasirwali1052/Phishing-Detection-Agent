def is_ddos_attack(features):
    """
    Apply rule-based logic to determine if the traffic log is a DDoS attack.
    Returns (is_ddos: bool, reason: str)
    """
    reasons = []

    if features["rate_per_minute"] > 300:
        reasons.append("High request rate > 300/min")

    if features["packet_size"] > 1000:
        reasons.append("Large packet size > 1000 bytes")

    if features["is_automated"]:
        reasons.append("Bot-like user-agent detected")

    if features["path"] in ["/index.html", "/login", "/register"]:
        reasons.append("Targeting sensitive endpoint")

    if len(reasons) >= 2:
        return True, " | ".join(reasons)

    return False, "Normal traffic"