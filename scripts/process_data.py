# scripts/process_data.py

import openai
from config.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def translate_and_summarize(title, description):
    prompt = f"Translate the following Hindi text to English and provide a summary:\n\nTitle: {title}\n\nDescription: {description}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
