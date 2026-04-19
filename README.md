# 🚀 LogLens AI

### From Raw Logs to Smart Decisions

---

## 📌 Overview

**LogLens AI** is an AI-powered cybersecurity tool that transforms raw network logs into **human-readable insights, correlated incidents, and actionable recommendations**.

It helps reduce incident response time by converting complex logs into **clear security intelligence**.

---

## 🎯 Problem Statement

Modern systems generate massive volumes of logs that are:

* ❌ Difficult to understand
* ⏳ Time-consuming to analyze
* 🧠 Hard for beginners and tiring for experts

➡️ Result: **Delayed threat detection and slow incident response**

---

## 💡 Solution

LogLens AI acts like a **virtual SOC analyst** by:

* 🔍 Parsing raw logs into structured data
* 🚨 Detecting anomalies (brute force, port scan)
* 🏷️ Classifying severity levels
* 🔗 Correlating events into incidents
* 🧠 Generating AI-based explanations
* 💡 Providing actionable recommendations

---

## 🧱 Architecture

```
Raw Logs
   ↓
Log Parsing (Regex)
   ↓
Structured Data (JSON)
   ↓
Anomaly Detection
   ↓
Log Classification
   ↓
Incident Correlation
   ↓
AI Explanation Engine
   ↓
Dashboard Output (Streamlit)
```

---

## 🔥 Features

### 🔍 Log Parsing

* Extracts:

  * Source IP
  * Port
  * Action
  * Timestamp

---

### 🚨 Anomaly Detection

Detects:

* Brute-force attacks
* Port scanning
* Suspicious patterns

---

### 🔗 Incident Correlation

Combines multiple logs into **attack stories**

Example:

> Multiple failed logins + multiple ports accessed → Coordinated attack

---

### 🧠 AI Insights

Example output:

> “Multiple failed SSH login attempts followed by port scanning indicate a potential brute-force attack.”

---

### 💡 Recommendations

* Block malicious IP
* Restrict access
* Enable firewall rules

---

### 📊 Dashboard

* Real-time metrics
* Charts (port usage, severity)
* Visual alerts
* Structured logs

---


## ⚙️ Tech Stack

* 🐍 Python
* 📊 Pandas
* 🔍 Regex
* 🤖 LLM (AI explanations)
* 🌐 Streamlit (UI Dashboard)
* 🧠 Scikit-learn (optional ML)

---

## 📂 Project Structure

```
H2H-Minion-LogLensAI/

├── Data/
│   └── sample_logs.txt
│
├── src/
│   ├── app.py
│   ├── parser.py
│   ├── classifier.py
│   ├── anomaly.py
│   ├── incident.py
│   ├── explainer.py
│   └── ip_intelligence.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/H2H-Minion-LogLensAI.git
cd H2H-Minion-LogLensAI
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
cd src
streamlit run app.py
```

---

## 📊 Example Output

```json
{
  "source_ip": "192.168.1.10",
  "port": 22,
  "action": "DENY",
  "category": "CRITICAL",
  "ip_type": "Private Network"
}
```

---

## ⏱️ Time-to-Clarity Metric

| Without Tool | With LogLens AI |
| ------------ | --------------- |
| 2–3 minutes  | < 10 seconds    |

---

## 🔐 Use Cases

* SOC (Security Operations Center)
* Incident response automation
* Threat detection
* SIEM enhancement

---

## 🔮 Future Scope

* ⚡ Real-time log streaming
* 💬 Chat-based log analysis
* 🌐 IP geolocation
* 🤖 Advanced ML models
* 🔗 Integration with tools like Splunk

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📜 License

MIT License

---
## 👥 Team

**Team Name:** Minion++

* Nikath Jahan
* Nisha S

---

