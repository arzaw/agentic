import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests
import json
from IPython.display import Markdown, display, update_display

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model configurations
gemini_model = "gemini-1.5-pro"  # Adjust based on your access
ollama_model = "llama3.2"  # Adjust based on what you have pulled locally

# System prompts
gemini_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

ollama_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

# Initialize conversation
gemini_messages = ["Hi there"]
ollama_messages = ["Hi"]

def call_gemini(messages):
    # Create the model with system instruction
    model = genai.GenerativeModel(
        model_name=gemini_model,
        system_instruction=gemini_system
    )
    
    # Start chat
    chat = model.start_chat(history=[])
    
    # Build conversation history
    for gemini, ollama in zip(gemini_messages, ollama_messages):
        chat.send_message(gemini)
        chat.send_message(ollama)
    
    # Get response to the latest ollama message
    response = chat.send_message(ollama_messages[-1])
    return response.text

def call_ollama(messages):
    # Prepare the chat history
    ollama_chat_messages = []
    for gemini, ollama in zip(gemini_messages[:-1], ollama_messages):
        ollama_chat_messages.append({"role": "user", "content": gemini})
        ollama_chat_messages.append({"role": "assistant", "content": ollama})
    
    # Add the latest message
    ollama_chat_messages.append({"role": "user", "content": gemini_messages[-1]})
    
    # Prepare the payload with system prompt
    payload = {
        "model": ollama_model,
        "messages": [
            {"role": "system", "content": ollama_system},
            *ollama_chat_messages
        ],
        "stream": False
    }
    
    # Make API call to local Ollama instance
    response = requests.post("http://localhost:11434/api/chat", json=payload)
    
    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Initial messages
print(f"Gemini:\n{gemini_messages[0]}\n")
print(f"Ollama:\n{ollama_messages[0]}\n")

# Conduct the conversation
for i in range(5):
    # Gemini's turn
    gemini_next = call_gemini(gemini_messages)
    print(f"Gemini:\n{gemini_next}\n")
    gemini_messages.append(gemini_next)
    
    # Ollama's turn
    ollama_next = call_ollama(gemini_messages)
    print(f"Ollama:\n{ollama_next}\n")
    ollama_messages.append(ollama_next)