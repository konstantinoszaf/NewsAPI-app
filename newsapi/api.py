from flask import Flask, jsonify, request, Blueprint
from newsapi.provider.provider_api import call_news_api
from newsapi.errors.provider_errors import NewsAPIError, NoKeyWordError, WrongKeyError

api = Blueprint("api", __name__)


@api.route("/news", methods=["POST"])
def news_api():
    try:
        data = request.get_json()
        keyword = fetch_keyword(data)
        if not keyword:
            raise NoKeyWordError
        title, url = call_news_api(keyword)
        return jsonify({"title": title, "url": url})

    except NewsAPIError as e:
        return {"error": e.errors.reason}, e.errors.status_code
    except NoKeyWordError:
        return {"error": "Keyword must not be empty"}, 400
    except WrongKeyError:
        return {"error": "Wrong key used"}, 406


def fetch_keyword(data: dict) -> str:
    try:
        keyword = data["keyword"]
    except Exception:
        raise WrongKeyError

    return keyword
