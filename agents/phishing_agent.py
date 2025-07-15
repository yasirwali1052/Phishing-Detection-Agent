from tools.vt_checker import check_url_with_virustotal
from tools.attachment_checker import is_suspicious_attachment
from tools.rule_engine import flag_suspicious_text

def phishing_agent(state: dict) -> dict:
    log = state.get("log", {})
    url_result = check_url_with_virustotal(log.get("url", ""))
    attachment_result = is_suspicious_attachment(log.get("attachment", ""))
    text_result = flag_suspicious_text(log.get("email_text", ""))

    return {
        "results": {
            "url_flag": url_result,
            "attachment_flag": attachment_result,
            "text_flag": text_result
        }
    }
