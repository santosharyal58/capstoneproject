from flask import Flask, render_template, request
from scripts.fetch_data import fetch_news_data
from scripts.process_data import translate_and_summarize

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    articles = fetch_news_data()
    processed_articles = []
    for article in articles:
        title = article.get('title')
        description = article.get('description')
        source=article.get('source_id')
        published=article.get('pubDate')
        if title and description:
            translated_summary = translate_and_summarize(title, description)
            processed_articles.append({
                'original_title': title,
                'original_description': description,
                'translated_summary': translated_summary,
                'source': source,
                'date': published
            })

    if request.method == 'POST':
        search_term = request.form.get('search', '').lower()
        filtered_articles = [
            article for article in processed_articles
            if search_term in article['original_title'].lower()
            or search_term in article['original_description'].lower()
        ]
        return render_template('index.html', articles=filtered_articles)

    return render_template('index.html', articles=processed_articles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)