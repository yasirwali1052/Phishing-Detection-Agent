from workflows.langgraph_phishing_flow import app

log_input = {
    "url": "http://paypal.verify-update.com",  # Fake phishing
    "attachment": "invoice.html",
    "email_text": "Please verify your account urgently."
}


response = app.invoke({"log": log_input})
print("\n🔍 Final Decision by LLM:\n", response["decision"])