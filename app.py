import os
import streamlit as st
from openai import OpenAI
from groq import Groq
from huggingface_hub import InferenceClient


st.set_page_config(page_title="LLM API Practice")

st.title("LLM API Practice")
st.write("Practice project using OpenAI, Groq, and Hugging Face APIs.")


question = st.text_input("Ask a question:")

provider = st.selectbox(
    "Choose API",
    ["OpenAI", "Groq", "Hugging Face Image"]
)


if st.button("Generate Response"):

    if not question.strip():
        st.warning("Please enter a question.")

    elif provider == "Hugging Face Image":

        api_key = os.getenv("HF_TOKEN")

        if not api_key:
            try:
                api_key = st.secrets["HF_TOKEN"]
            except Exception:
                api_key = None

        if not api_key:
            st.error("HF_TOKEN is not configured.")

        else:
            client = InferenceClient(
                provider="fal-ai",
                api_key=api_key
            )

            image = client.text_to_image(
                prompt=question,
                model="black-forest-labs/FLUX.1-schnell"
            )

            st.subheader("Generated Image")
            st.image(image)


    elif provider == "OpenAI":

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            try:
                api_key = st.secrets["OPENAI_API_KEY"]
            except Exception:
                api_key = None

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


    elif provider == "Groq":

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            try:
                api_key = st.secrets["GROQ_API_KEY"]
            except Exception:
                api_key = None

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
                )

                st.subheader("Response")
                st.write(response.choices[0].message.content)
