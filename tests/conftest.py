import pytest
import os
import sys

from newsapi.app import create_app

root = os.path.join(os.path.dirname(__file__))
package = os.path.join(root, '..')
sys.path.insert(0, os.path.abspath(package))


@pytest.fixture(scope='session', autouse=True)
def app(request):
    app = create_app({
        'TESTING': True
    })
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def client(app, request):
    return app.test_client()
