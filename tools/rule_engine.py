def flag_suspicious_text(text: str) -> bool:
    suspicious_keywords = ["verify now", "login", "urgent", "account suspended", "click here"]
    return any(keyword in text.lower() for keyword in suspicious_keywords)
