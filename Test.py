import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=api_key)

def testmodel():
    import google.generativeai as genai
    genai.configure(api_key=api_key)

    models=genai.list_models()
    for model in models:
        print(f"{model.name} - {model.supported_generation_methods}")

testmodel()