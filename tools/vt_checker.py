import os
import requests
from dotenv import load_dotenv
load_dotenv()
import base64

def check_url_with_virustotal(url: str) -> str:
    api_key = os.getenv("VT_API_KEY")
    headers = {"x-apikey": api_key}

    # Submit the URL for analysis (if not already present)
    submit_url = "https://www.virustotal.com/api/v3/urls"
    response = requests.post(submit_url, headers=headers, data={"url": url})
    if response.status_code != 200:
        print("VirusTotal submit error:", response.status_code, response.text)
        return "error"

    # Encode the URL for lookup
    url_id = base64.urlsafe_b64encode(url.encode()).decode().rstrip("=")
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
