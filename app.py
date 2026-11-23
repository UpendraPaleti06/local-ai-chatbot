# app.py - Version 2: the same chatbot as a web page
import ollama
import streamlit as st

MODEL = "llama3.2"  # change to "llama3.2:1b" if that is the model you downloaded
SYSTEM_PROMPT = "You are a friendly, helpful assistant. Keep answers short and clear."


def stream_reply(messages):
    """Send the whole conversation to the model and hand back its answer piece by piece."""
    for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
        yield chunk["message"]["content"]


st.title("My Local AI Chatbot")
st.caption(f"Running {MODEL} on my own Mac with Ollama. Nothing leaves this computer.")

# Streamlit re-runs this whole file every time you send a message.
# st.session_state is a notebook that survives those re-runs, so the chat history lives there.
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Show the conversation so far (the hidden system instruction is skipped)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# The chat box at the bottom of the page
prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        reply = st.write_stream(stream_reply(st.session_state.messages))

    st.session_state.messages.append({"role": "assistant", "content": reply})
