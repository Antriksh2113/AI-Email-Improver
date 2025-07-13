import streamlit as st
import requests

st.set_page_config(page_title="AI Email Improver", layout="centered")

st.title("AI Email Improver")
st.markdown("Rewrite your email drafts with AI in different tones.")

tone = st.selectbox("Choose Tone", ["Formal", "Polite", "Friendly", "Concise", "Persuasive"])
draft = st.text_area("Paste your rough email draft here:", height=200)

if st.button("Rewrite Email"):
    if not draft.strip():
        st.warning("Please enter an email draft.")
    else:
        with st.spinner("Contacting AI and rewriting..."):
            try:
                response = requests.post(
                    "http://localhost:8000/rewrite",
                    json={"draft": draft, "tone": tone}
                )
                if response.status_code == 200:
                    rewritten = response.json()["rewritten_email"]
                    st.subheader("Rewritten Email")
                    st.success(rewritten)
                else:
                    st.error("Failed to rewrite email. Please try again.")
            except Exception as e:
                st.error(f"Error: {e}")
