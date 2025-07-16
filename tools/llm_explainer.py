from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"  
)

def llm_ddos_detector(log: dict) -> tuple:
    """
    Use Groq LLM via LangChain to detect DDoS attack from a raw log.
    Returns: (bool, explanation)
    """
    prompt = f"""
You are a cybersecurity SOC analyst.

Here is a traffic log:
{log}

1. Is this a DDoS attack? (Yes or No)
2. Explain why.

Reply format:
DDoS: Yes/No
Reason: <your explanation>
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    content = response.content.strip().lower()
    is_ddos = "yes" in content.splitlines()[0]
    reason = "\n".join(content.splitlines()[1:]).replace("reason:", "").strip()

    return is_ddos, reason