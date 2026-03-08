import streamlit as st
from openai import OpenAI

# OpenRouter Client
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Page settings
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")

    model = st.selectbox(
        "Choose Model",
        [
            "openai/gpt-3.5-turbo",
            "mistralai/mistral-7b-instruct",
            "meta-llama/llama-3-8b-instruct"
        ]
    )

    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.markdown("Built by **Dhamini** 🚀")

# Main Title
st.title("🤖 AI Chat Assistant")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        response = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            temperature=temperature
        )

        answer = response.choices[0].message.content
        message_placeholder.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )