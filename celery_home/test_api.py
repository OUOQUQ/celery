from app import app
import pytest
import json


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_get(client):
    response = client.get('/star?star=5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'task_id' in data


def test_post(client):
    response = client.post('/add', json={'num1': 5, 'num2': 10})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'task_id' in data


def test_celery_test(client):
    response = client.get('/celery_test?task_id=4398067b-cf9c-42c6')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'state' in data
    assert data['state'] == 'PENDING'