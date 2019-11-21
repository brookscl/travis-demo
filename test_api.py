from app import api_app

import pytest


@pytest.fixture(scope='module')
def client():
    testing_client = api_app.test_client()

    # Establish an application context before running the tests.
    ctx = api_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_index_returns_success(client):
    client.get('/').status_code == 200


def test_index_is_hello_world(client):
    response = client.get('/')
    assert b"Hello" in response.data


def test_api_cat_breeds_index_success(client):
    response = client.get('api/cat-breeds/')
    assert response.status_code == 200


def test_api_cat_breeds_three_breeds(client):
    response = client.get('api/cat-breeds/')
    assert len(response.json) == 3


def test_fail():
    assert False
