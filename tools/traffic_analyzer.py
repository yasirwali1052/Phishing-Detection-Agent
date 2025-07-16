def extract_features(log):
    """
    Extract important traffic features from the input log.
    """
    return {
        "src_ip": log.get("src_ip"),
        "dst_ip": log.get("dst_ip"),
        "timestamp": log.get("timestamp"),
        "request_type": log.get("request_type", "").upper(),
        "path": log.get("path", ""),
        "user_agent": log.get("user_agent", "").lower(),
        "packet_size": log.get("packet_size", 0),
        "rate_per_minute": log.get("rate_per_minute", 0),
        "is_automated": any(bot in log.get("user_agent", "").lower() for bot in ["curl", "python", "requests", "httpclient"])
    }