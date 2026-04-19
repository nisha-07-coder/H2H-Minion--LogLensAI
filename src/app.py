import streamlit as st
import os
import pandas as pd

from parser import parse_file
from classifier import classify_logs
from anomaly import detect_anomalies
from explainer import explain_anomalies
from incident import correlate_incidents
from ip_intelligence import enrich_logs

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="LogLens AI", layout="wide")

# ------------------ CUSTOM STYLING ------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("🚀 LogLens AI")
st.subheader("From Raw Logs to Smart Decisions")

st.divider()

# ------------------ FILE PATH ------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "Data", "sample_logs.txt")

# ------------------ PIPELINE ------------------
logs = parse_file(file_path)
logs = enrich_logs(logs)
logs = classify_logs(logs)

anomalies = detect_anomalies(logs)
explanations = explain_anomalies(anomalies)
incidents = correlate_incidents(anomalies)

df = pd.DataFrame(logs)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🔍 LogLens Controls")
st.sidebar.write("📁 Sample Logs Loaded")
st.sidebar.write("⚙️ Filtering (Coming Soon)")
st.sidebar.write("🌐 Real-time Monitoring (Future)")

# ------------------ METRICS ------------------
st.write("## 📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📄 Total Logs", len(logs))
col2.metric("🚨 Anomalies", len(anomalies))
col3.metric("🔥 Incidents", len(incidents))

st.divider()

# ------------------ LOG TABLE ------------------
st.write("## 📄 Classified Logs")
st.dataframe(df, use_container_width=True)

st.divider()

# ------------------ ANOMALIES ------------------
st.write("## 🚨 Detected Anomalies")

if anomalies:
    for a in anomalies:
        st.error(f"""
🚨 **{a['type']}**
- IP: {a['ip']}
- Detail: {a['detail']}
""")
else:
    st.success("✅ No anomalies detected")

st.divider()

# ------------------ INCIDENTS ------------------
st.write("## 🔗 Correlated Incidents")

if incidents:
    for i in incidents:
        st.warning(f"""
⚠️ **{i['incident']}**
- IP: {i['ip']}
- Detail: {i['detail']}
""")
else:
    st.success("✅ No incidents detected")

st.divider()

# ------------------ AI INSIGHTS ------------------
st.write("## 🧠 AI Insights & Recommendations")

for e in explanations:
    st.success(e)

st.divider()

# ------------------ CHARTS ------------------
st.write("## 📊 Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.write("### Traffic by Port")
    st.bar_chart(df["port"].value_counts())

    st.write("### Traffic by Action")
    st.bar_chart(df["action"].value_counts())

with col2:
    st.write("### Severity Distribution")
    st.bar_chart(df["category"].value_counts())

    st.write("### IP Type Distribution")
    st.bar_chart(df["ip_type"].value_counts())

st.divider()

# ------------------ FOOTER ------------------
st.markdown("""
---
🔐 **LogLens AI** | Built for Cybersecurity Analysis  
""")