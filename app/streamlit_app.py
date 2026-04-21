import streamlit as st
import pandas as pd
from main import run_pipeline, run_query

st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("AI Data Analyst")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "df_clean" not in st.session_state:
    st.session_state.df_clean = None

if "charts" not in st.session_state:
    st.session_state.charts = None

if "plan" not in st.session_state:
    st.session_state.plan = None



file = st.file_uploader("Upload your dataset", type=["csv"])

if file is not None and st.session_state.df_clean is None:
    df_preview = pd.read_csv(file)

    st.subheader("Preview")
    st.dataframe(df_preview.head())

    file.seek(0)

    with st.spinner("Analyzing dataset..."):
        df_clean, charts, plan, insights = run_pipeline(file)

   
    st.session_state.df_clean = df_clean
    st.session_state.charts = charts
    st.session_state.plan = plan

   
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"### 📊 Insights\n{insights}"
    })

    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if st.session_state.plan:
    with st.expander("🧠 View Analysis Plan"):
        st.markdown(st.session_state.plan)


if st.session_state.df_clean is not None:
    user_input = st.chat_input("Ask anything about your data...")

    if user_input:
     
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

     
        code, result = run_query(st.session_state.df_clean, user_input)

        response = f"**Result:**\n{result}"

     
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()


if st.session_state.charts:
    st.divider()
    st.subheader("📊 Data Overview")

    cols = st.columns(2)

    for i, fig in enumerate(st.session_state.charts):
        with cols[i % 2]:
            st.pyplot(fig)