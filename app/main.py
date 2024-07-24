import requests
import json
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

API_KEY = '6a3277ad0ab04bbabc7b6cd1f9b51fad'
URL = 'https://newsapi.org/v2/everything'

def fetch_articles(api_key, country='ar', page_size=100):
    params = {
        'apiKey': api_key,
        'q': '*',
        'language': 'es',
        'pageSize': page_size,
        'sortBy': 'publishedAt'
    }
    response = requests.get(URL, params=params)
    data = response.json()
    if data['status'] == 'ok':
        return data['articles']
    else:
        raise Exception('Error fetching data from NewsAPI')

articles = fetch_articles(API_KEY)

def extract_info(article):
    return {
        'title': article.get('title'),
        'author': article.get('author'),
        'published_at': article.get('publishedAt'),
        'source': article['source'].get('name'),
        'content': article.get('content')
    }

def get_keywords(text):
    stop_words = set(stopwords.words('spanish'))
    words = word_tokenize(text.lower())
    keywords = [word for word in words if word.isalnum() and word not in stop_words]
    return keywords

def categorize_article(title, content):

    categories = {
        'política': ['política', 'gobierno', 'elecciones'],
        'economía': ['economía', 'mercado', 'finanzas'],
        'deportes': ['deporte', 'fútbol', 'juego']
    }
    article_text = title.lower() + ' ' + (content.lower() if content else '')
    for category, keywords in categories.items():
        if any(keyword in article_text for keyword in keywords):
            return category
    return 'otros'

# Extracción de información y categorización
processed_articles = [extract_info(article) for article in articles]
for article in processed_articles:
    article['keywords'] = get_keywords(article['title'] + ' ' + (article['content'] if article['content'] else ''))
    article['category'] = categorize_article(article['title'], article['content'])

def analyze_data(articles):
    # Frecuencia por fuente
    sources_freq = Counter([article['source'] for article in articles])

    # Palabras clave más frecuentes
    all_keywords = [keyword for article in articles for keyword in article['keywords']]
    keywords_freq = Counter(all_keywords).most_common(10)

    # Frecuencia por categoría
    category_freq = Counter([article['category'] for article in articles])

    return {
        'sources_freq': sources_freq,
        'keywords_freq': keywords_freq,
        'category_freq': category_freq
    }

analysis = analyze_data(processed_articles)

def generate_report(analysis, file_name='report.json'):
    report = {
        'total_articles': len(processed_articles),
        'keywords_freq': analysis['keywords_freq'],
        'top_categories': analysis['category_freq'].most_common(5),
        'sources_freq': analysis['sources_freq']
    }
    with open(file_name, 'w') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

generate_report(analysis)
