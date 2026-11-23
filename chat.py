# chat.py - Version 1: a chatbot that runs in Terminal
import ollama

MODEL = "llama3.2"  # change to "llama3.2:1b" if that is the model you downloaded

# The conversation so far. The bot "remembers" by re-reading this whole list every time.
messages = [
    {"role": "system", "content": "You are a friendly, helpful assistant. Keep answers short and clear."}
]

print("Local chatbot ready! Type a message and press Return. Type 'quit' to stop.\n")

while True:
    user_text = input("You: ")

    if user_text.strip().lower() in ("quit", "exit", "bye"):
        print("Bot: Goodbye!")
        break
    if not user_text.strip():
        continue

    messages.append({"role": "user", "content": user_text})

    print("Bot: ", end="", flush=True)
    reply = ""
    for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
        piece = chunk["message"]["content"]
        print(piece, end="", flush=True)
        reply += piece
    print("\n")

    messages.append({"role": "assistant", "content": reply})
