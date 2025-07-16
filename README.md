
# 🛡️ Phishing Detection Agent – Powered by LangGraph + Groq

This project is a lightweight **AI-powered phishing detection pipeline** built using **LangGraph**, **Groq LLMs**, and **external threat intelligence tools** like VirusTotal.

It processes suspicious **email logs** in real time by checking:
- 🕵️ Malicious URLs
- 📎 Dangerous attachments
- 🧠 Phishing keywords or phrases

## 🚀 Key Features

- ✅ **Modular Agents**: Each agent handles a specific check (URL, file, text)
- 🔄 **LangGraph StateFlow**: Orchestrates agents in a directed flow using `StateGraph`
- 🤖 **LLM Reasoning**: Uses Groq's fast & affordable LLM to make final phishing decisions
- 🧪 **VirusTotal Integration**: Real-time threat scoring for suspicious links

---

## 📁 Project Structure

```

cyber\_ai\_soc/
├── agents/
│   └── phishing\_agent.py         # Main agent logic
├── tools/
│   ├── vt\_checker.py             # VirusTotal URL scanner
│   ├── attachment\_checker.py     # Flags risky file extensions
│   └── rule\_engine.py            # Detects phishing keywords
├── workflows/
│   └── langgraph\_phishing\_flow\.py  # LangGraph node flow
├── .env                          # API keys (Groq + VirusTotal)
├── main.py                       # Run the pipeline with sample log
├── requirements.txt              # All dependencies

```

---

## 🧠 How It Works

1. 📨 **Input**: A suspicious log is received containing:
   - URL
   - File attachment name
   - Email text

2. 🧩 **Tools** check:
   - `vt_checker.py`: Queries VirusTotal API for the URL
   - `attachment_checker.py`: Flags file types like `.html`, `.exe`, etc.
   - `rule_engine.py`: Checks for text like `"verify now"`, `"urgent"`, etc.

3. 🧠 **LangGraph StateGraph**:
   - Runs `phishing_agent.py` first
   - Then calls `llm_reasoner()` using Groq's **Mixtral** model to reason over the results

4. 📢 **Final Output**:
   - LLM responds: "This is a phishing attack" or "Looks safe"
   - Full reasoning is printed

---

## 🌐 API Keys Setup

Create a `.env` file:

```

GROQ\_API\_KEY=your\_groq\_key\_here
VT\_API\_KEY=your\_virustotal\_key\_here

````

---

## 📦 Installation & Usage

```bash
# Step 1: Clone the repo
git clone https://github.com/yasirwali1052/Phishing-Detection-Agent.git
cd Phishing-Detection-Agent

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Linux/Mac

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Add .env file with API keys

# Step 5: Run the pipeline
python main.py


---

## 🛠️ Future Enhancements

* Add support for DDoS and user behavior anomaly detection
* Real-time alerts and report generation
* Streamlit dashboard for monitoring



## 👤 Author

**Yasir Wali**
📍 NUML Islamabad | B.S. in AI
🌐 [GitHub](https://github.com/yasirwali1052) | 💼 [LinkedIn](https://www.linkedin.com/in/yasirwali1052)


### ✅ How to Add to Your Repo

1. Save this as `README.md` in your project folder.
2. Then run in CMD:

```bash
git add README.md
git commit -m "Add project documentation"
git push
````

Let me know if you want:

* A `Streamlit` UI added later
* A badge and GitHub project topics
* A video or image preview section in the README

You're doing excellent — this README is professional and complete!

