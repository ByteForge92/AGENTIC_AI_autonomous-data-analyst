# 🤖 Autonomous AI Data Analyst

An agentic AI system that analyzes datasets, generates insights, and allows users to interact with data using natural language.

---

## 🚀 Features

- 📊 Automatic dataset analysis
- 🧠 AI-generated insights
- 💬 Chat-based querying (Natural Language Queries)
- 🔍 Autonomous analysis planning
- 📈 Data visualizations
- 🤖 Agent-like behavior (planner + execution + explanation)

---

## 🧠 Architecture

- **Planner Agent** → decides what to analyze
- **Analysis Engine (Pandas)** → processes full dataset
- **AI Insight Generator** → explains patterns
- **NLQ Engine** → converts questions to code
- **Streamlit UI** → chat-based interface

---

## ⚙️ Tech Stack

- Python
- Pandas
- Streamlit
- Groq (LLM)
- Matplotlib

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
