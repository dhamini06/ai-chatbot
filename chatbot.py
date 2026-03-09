import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

# Get API key from Streamlit secrets
try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    st.error("API key not found. Please add OPENROUTER_API_KEY in Streamlit Secrets.")
    st.stop()

# Initialize OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Sidebar settings
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

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.markdown("Built by **Dhamini** 🚀")

# App title
st.title("🤖 AI Chat Assistant")

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        try:
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                temperature=temperature
            )

            answer = response.choices[0].message.content

        except Exception as e:
            answer = "⚠️ Error connecting to AI service."

        message_placeholder.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )