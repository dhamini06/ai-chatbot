# AI Chat Assistant

A conversational AI chatbot built using Python, Streamlit, and OpenRouter APIs.

## Features
- Interactive AI chat interface
- Conversation memory
- Model selection from sidebar
- Adjustable response creativity
- Clean modern UI

## Tech Stack
Python
Streamlit
OpenRouter API
LLM Models (GPT / Mistral / Llama)

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run the chatbot:

streamlit run chatbot.py

## Project Architecture

User → Streamlit UI → Python Backend → OpenRouter API → AI Model → Response

## Future Improvements
- Streaming responses (typing effect)
- Chat with PDF documents
- Persistent chat history
- Deployment with authentication
