from langgraph.graph import StateGraph, END
from agents.phishing_agent import phishing_agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict, Dict, Any, Optional
import os
import requests
import base64
load_dotenv()

class PhishingState(TypedDict, total=False):
    log: Dict[str, Any]
    results: Dict[str, Any]
    decision: Optional[str]

state_schema = PhishingState

def llm_reasoner(state: dict) -> dict:
    results = state.get("results", {})
    prompt = f"""
    Analyze the following phishing indicators:
    - URL: {results['url_flag']}
    - Attachment: {results['attachment_flag']}
    - Text: {results['text_flag']}
    Is this a phishing attack? Give a short reason.
    """
    llm = ChatGroq(model="Llama3-8b-8192")
    response = llm.invoke(prompt)
    return {"decision": response.content.strip()}

def check_url_with_virustotal(url: str) -> str:
    api_key = os.getenv("VT_API_KEY")
    headers = {"x-apikey": api_key}

    # Submit the URL for analysis (if not already present)
    submit_url = "https://www.virustotal.com/api/v3/urls"
    response = requests.post(submit_url, headers=headers, data={"url": url})
    if response.status_code != 200:
        print("VirusTotal submit error:", response.status_code, response.text)
        return "error"

    # Base64 encode the URL for lookup (URL-safe, no padding)
    url_bytes = url.encode()
    url_id = base64.urlsafe_b64encode(url_bytes).decode().rstrip("=")
    lookup_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
    response = requests.get(lookup_url, headers=headers)
    print("VirusTotal lookup status:", response.status_code, response.text)
    if response.status_code != 200:
        return "error"
    data = response.json()

    verdict = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
    if verdict.get("malicious", 0) > 0:
        return "malicious"
    return "clean"

# Define the graph
builder = StateGraph(state_schema)
builder.add_node("phishing_check", phishing_agent)
builder.add_node("llm_reason", llm_reasoner)
builder.set_entry_point("phishing_check")
builder.add_edge("phishing_check", "llm_reason")
builder.add_edge("llm_reason", END)

app = builder.compile() 