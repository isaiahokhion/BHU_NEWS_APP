from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"

API_KEY = '5d2d06676ea44fe1a331b63270e8f4a7'
NEWS_API_URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

@app.route('/')
def index():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
    else:
        articles = []
    return render_template('home.html', articles=articles)

@app.route('/api/news')
def api_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch news'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
