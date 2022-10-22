from datetime import date
from typing import Tuple
from newsapi.errors.provider_errors import NewsAPIError
import requests


def call_news_api(keyword: str) -> Tuple:

    api_key = "e34c9fc42115415a8cfcb4acc9cf0d7c"
    api_url = f"https://newsapi.org/v2/everything?q={keyword}&from={date.today()}&sortBy=popularity&apiKey={api_key}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        title = data["articles"][0]["title"]
        url = data["articles"][0]["url"]
        return title, url
    else:
        raise NewsAPIError(errors=response)
