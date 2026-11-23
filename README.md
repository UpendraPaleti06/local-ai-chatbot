# Local AI Chatbot

A private chatbot that runs entirely on my Mac. It uses Ollama to run Meta's Llama 3.2 model locally, with two interfaces: a Terminal chat (chat.py) and a web app built with Streamlit (app.py).

## What it shows
- Running an open-source LLM locally with Ollama: no API keys, no cloud costs
- Conversation memory by re-sending the message history (system, user and assistant roles)
- Streaming responses as they are generated
- A chat interface with Streamlit session state

## How to run
1. Install Ollama from ollama.com, then run: ollama pull llama3.2
2. python3 -m venv .venv && source .venv/bin/activate
3. pip install -r requirements.txt
4. Terminal version: python chat.py
5. Web version: streamlit run app.py
