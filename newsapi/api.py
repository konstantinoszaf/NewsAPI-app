from flask import Flask, jsonify, request
from newsapi.provider.provider_api import call_news_api
app = Flask(__name__)


@app.route('/news', methods=['POST'])
def news_api():

    data = request.get_json()
    keyword = data['keyword']
    title, url = call_news_api(keyword)
    return jsonify({'title': title, 'url': url})

