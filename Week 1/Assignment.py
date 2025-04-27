from google import genai
import requests

client = genai.Client(api_key="AIzaSyBZL3ZOkZNW3y39q4FAjlvRz5KxD0udxPk")

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

# Get gemini-2.5 to answer, with streaming

response = client.models.generate_content(
    model = "models/gemini-2.5-pro-exp-03-25",
    contents=question
)

print(f"Response from gemini-2.5: {response.text}")

# Get Llama 3.2 to answer

url = "http://localhost:11434/api/chat"  # Note: using /api/chat instead of /api/generate

payload = {
    "model": "llama3.2", 
    "messages": [
        {"role": "user", "content": question}
    ],
    "stream": False 
}

response_ollama = requests.post(url, json=payload)

result = response_ollama.json()
# print(result)
print(f'Response from Ollama: {result["message"]["content"]}')