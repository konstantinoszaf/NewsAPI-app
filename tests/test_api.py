import pytest
import responses


def test_200_news_api(client) -> None:
    response = client.post("/news", json={"keyword": "greece"})
    assert response.status_code == 200


def test_no_keyword_error_news_api(client) -> None:
    response = client.post("/news", json={"keyword": ""})
    assert response.status_code == 400


def test_wrong_keyword_error_news_api(client) -> None:
    response = client.post("/news", json={"wrong_key": "some key"})
    assert response.status_code == 406


"""
Could not find all the news API errors in the documentation so i created some custom ones.
"""


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ({"error": "Unauthorized"}, 401),
        ({"error": "some error1"}, 500),
        ({"error": "some error2"}, 404),
        ({"error": "some error3"}, 400),
    ],
)
@responses.activate
def test_errors_from_api_news_api(client, test_input, expected) -> None:
    responses.add(
        responses.GET,
        "https://newsapi.org/v2/everything",
        json=test_input,
        status=expected,
    )
    response = client.post("/news", json={"keyword": "foo"})
    assert response.status_code == expected
