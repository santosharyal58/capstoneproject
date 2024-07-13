# app.py

from flask import Flask, render_template
from scripts.fetch_data import fetch_news_data
from scripts.process_data import translate_and_summarize

app = Flask(__name__)

@app.route('/')
def index():
    articles = fetch_news_data()
    processed_articles = []
    for article in articles:
        title = article.get('title')
        description = article.get('description')
        if title and description:
            translated_summary = translate_and_summarize(title, description)
            processed_articles.append({
                'original_title': title,
                'original_description': description,
                'translated_summary': translated_summary
            })
    return render_template('index.html', articles=processed_articles)

if __name__ == "__main__":
    app.run(debug=True)
