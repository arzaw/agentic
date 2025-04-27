import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

message = "Hello, Flash! This is my first ever message to you! Hi!"

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

ed = Website("https://edwarddonner.com")

system_prompt = "You are a cat that analyzes the contents of a website \
 and provides a short summary, ignoring text that might be navigation related. \
 Respond in markdown."


def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def summarize(url):
    website = Website(url)
    response = client.models.generate_content(
        model = "models/gemini-2.5-pro-exp-03-25",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.5,
        ),
        contents=user_prompt_for(website)
    )
    return response.text

print(summarize("https://arzaw.github.io/coursera-test/"))
