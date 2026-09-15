import os
import streamlit as st
from openai import OpenAI
from groq import Groq

st.set_page_config(page_title="LLM API Practice")

st.title("LLM API Practice")
st.write("Practice project using OpenAI and Groq APIs.")

question = st.text_input("Ask a question:")

provider = st.selectbox(
    "Choose API",
    ["OpenAI", "Groq"]
)

if st.button("Generate Response"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        if provider == "OpenAI":
            api_key = os.getenv("OPENAI_API_KEY")

            if not api_key:
                st.error("OPENAI_API_KEY is not configured.")
            else:
                client = OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-5.4",
                    messages=[
                        {"role": "user", "content": question}
                    ]
                )

                st.subheader("Response")
                st.write(response.choices[0].message.content)

        else:
            api_key = os.getenv("GROQ_API_KEY")

            if not api_key:
                st.error("GROQ_API_KEY is not configured.")
            else:
                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {"role": "user", "content": question}
                    ]
                )

                st.subheader("Response")
                st.write(response.choices[0].message.content)
