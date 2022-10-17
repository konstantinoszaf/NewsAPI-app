import pytest


def test_200_news_api(client) -> None:
    response = client.post('/news', data={'keyword': 'greece'})
    assert response.status_code == 200


