from flask import Flask, jsonify, request
from newsapi.provider.provider_api import call_news_api
from newsapi.errors.provider_errors import NewsAPIError, UnknownError, NoKeyWordError

app = Flask(__name__)


@app.route('/news', methods=['POST'])
def news_api():
    try:
        data = request.get_json()
        keyword = data['keyword']
        if not keyword:
            raise NoKeyWordError
        title, url = call_news_api(keyword)
        return jsonify({'title': title, 'url': url})

    except NewsAPIError as e:
        return {'error': e.errors.reason}, e.errors.status_code
    except NoKeyWordError:
        return {'error': 'Keyword must not be empty'}, 401
    except UnknownError:
        return {'error': 'There was an unknown error'}, 500
