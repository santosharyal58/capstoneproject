# scripts/fetch_data.py

import requests
from config.config import NEWSDATA_URL

def fetch_news_data():
    response = requests.get(NEWSDATA_URL)
    if response.status_code == 200:
        news_data = response.json()
        if news_data.get('status') == 'success':
            return news_data.get('results', [])
        else:
            print("Error in API response status")
    else:
        print("Error fetching data from the source")
    return []

