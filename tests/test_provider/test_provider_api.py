import pytest
from newsapi.provider.provider_api import call_news_api
import responses
from newsapi.errors.provider_errors import NewsAPIError

response_data = {"status":"ok",
                 "totalResults":9266,
                 "articles":
                     [{"source":
                           {"id":"engadget",
                            "name":"Engadget"},
                       "author":"Jon Fingas",
                       "title":"Apple Card users can soon sign up for a 'high-yield' savings account",
                       "description":"foo",
                       "url":"https://www.engadget.com/apple-card-savings-account-160055471.html",
                       "urlToImage":"irrelevant",
                       "publishedAt":"2022-10-13T16:00:55Z",
                       "content":"foo"}]}


title = 'Apple Card users can soon sign up for a \'high-yield\' savings account'
url = 'https://www.engadget.com/apple-card-savings-account-160055471.html'


@responses.activate
def test_200_call_news_api(client) -> None:
    responses.add(responses.GET,
                  'https://newsapi.org/v2/everything',
                  response_data,
                  status=200
                  )
    response = client.post('/news', json={'keyword': 'foo'})
    assert response.status_code == 200
    assert title, url == call_news_api('foo')


@responses.activate
def test_error_call_news_api(client) -> None:
    responses.add(responses.GET,
                  'https://newsapi.org/v2/everything',
                  response_data,
                  status=401
                  )
    with pytest.raises(NewsAPIError):
        call_news_api('foo')
