# scripts/process_data.py

import openai
from config.config import OPENAI_API_KEY

openai.api_key = 'sk-proj-Fa8cDCTkXdg2Nmj2JxtcT3BlbkFJmWkaQeRxDy3goJpDneeR'

def translate_and_summarize(title, description):
    prompt = f"Translate the following Hindi text to English and provide a summary:\n\nTitle: {title}\n\nDescription: {description}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content'].strip()