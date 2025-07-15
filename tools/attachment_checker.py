def is_suspicious_attachment(filename: str) -> bool:
    suspicious_exts = [".exe", ".html", ".php", ".js", ".bat", ".zip"]
    return any(filename.lower().endswith(ext) for ext in suspicious_exts)
