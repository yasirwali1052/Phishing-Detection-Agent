

# 🛡️ AI Threat Detection Agent – Powered by LangGraph + Groq

This project is a lightweight **AI-powered cyber threat detection pipeline** built using **LangGraph**, **Groq LLMs**, and **external tools** like **VirusTotal**.
It supports **real-time phishing email analysis** as well as **DDoS traffic pattern detection** using a hybrid rule + LLM approach.

---

## 🚨 What It Detects

* 🕵️ **Phishing Emails**

  * Malicious URLs
  * Dangerous file attachments
  * Suspicious keywords or phrases

* 🌐 **DDoS Attacks**

  * High-rate, large-packet network traffic
  * Automated bot behavior
  * LLM-assisted traffic analysis and explanation

---

## 🚀 Key Features

* ✅ **Modular Agents**: Each agent handles a specific task (phishing or DDoS)
* 🔄 **LangGraph StateFlow**: Directs how agents process inputs
* 🧠 **LLM Reasoning**: Uses Groq's Mixtral/LLama3 via LangChain for context-aware analysis
* 🔗 **VirusTotal Integration**: For real-time phishing URL threat scoring

---

## 📁 Project Structure

```
cyber_ai_soc/
├── agents/
│   ├── phishing_agent.py          # Phishing logic
│   └── ddos_agent.py              # DDoS logic (rule + LLM)
│
├── tools/
│   ├── vt_checker.py              # VirusTotal scanner
│   ├── attachment_checker.py      # Flags risky file types
│   ├── rule_engine.py             # Phishing keyword rules
│   ├── traffic_analyzer.py        # Extracts traffic features
│   ├── ddos_rules.py              # Rule-based DDoS detection
│   └── llm_explainer.py           # Groq LLM-based DDoS explanation
│
├── workflows/
│   ├── langgraph_phishing_flow.py # LangGraph flow for phishing
│   └── langgraph_ddos_flow.py     # LangGraph flow for DDoS
│
├── data/
│   └── sample_traffic.json        # Sample DDoS traffic logs
│
├── main.py                        # Unified entry to test both agents
├── .env                           # API keys (Groq + VirusTotal)
├── requirements.txt               # All dependencies
└── README.md                      # This file
```

---

## 🧠 How It Works

### 🟪 Phishing Detection Pipeline

1. **Input**: A suspicious email log with URL, attachment, and message text
2. **Tools**:

   * `vt_checker.py`: Checks URL via VirusTotal API
   * `attachment_checker.py`: Flags `.exe`, `.html`, etc.
   * `rule_engine.py`: Detects phishing keywords like `urgent`, `verify`
3. **LLM Reasoning**:

   * Groq LLM evaluates all signals to confirm if phishing
4. **LangGraph** coordinates the flow and final verdict

---

### 🟥 DDoS Detection Pipeline

1. **Input**: JSON traffic logs with IPs, rates, sizes, etc.
2. **Tools**:

   * `traffic_analyzer.py`: Extracts request type, size, rate
   * `ddos_rules.py`: Flags high-rate + bot-like behavior
   * `llm_explainer.py`: Groq LLM detects deeper pattern from log
3. **LangGraph** flow and `ddos_agent.py` combine both methods for final decision

---

## 🌐 API Keys Setup

Create a `.env` file in the project root with:

```
GROQ_API_KEY=your_groq_key_here
VT_API_KEY=your_virustotal_key_here
```

---

## 📦 Installation & Usage

```bash
# Step 1: Clone the repo
git clone https://github.com/yasirwali1052/Phishing-Detection-Agent.git
cd Phishing-Detection-Agent

# Step 2: Set up virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On Linux/Mac

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Add your .env file

# Step 5: Run either detection mode
python agents/phishing_agent.py        # For phishing detection
python agents/ddos_agent.py            # For DDoS detection
python workflows/langgraph_ddos_flow.py # LangGraph flow
```

Or run all via:

```bash
python main.py
```

---


---

## 👤 Author

**Yasir Wali**
📍 NUML Islamabad | B.S. in AI
🌐 [GitHub](https://github.com/yasirwali1052)
💼 [LinkedIn](https://www.linkedin.com/in/yasirwali1052)


