from datetime import date
from typing import Tuple
import requests


def call_news_api(keyword: str) -> Tuple:
    api_url = 'https://newsapi.org/v2/everything'

    request_data = {
        'q': keyword,
        'from': date.today(),
        'sortBy': 'popularity',
        'apiKey': 'e34c9fc42115415a8cfcb4acc9cf0d7c',
        'pageSize': 1
    }
    response = requests.get(api_url, params=request_data)
    data = response.json()
    title = data['articles'][0]['title']
    url = data['articles'][0]['url']
    return title, url
