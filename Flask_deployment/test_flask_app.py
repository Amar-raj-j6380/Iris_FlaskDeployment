import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):    
    resp = client.get('/hello')
    assert resp.json=={"message": "Hi there, I'm not working!!"}

def test_predict(client):
    test_data={
    "sepal_length":11,
    "sepal_width":12,
    "petal_length":1,
    "petal_width":12}
    resp=client.post('/predict', json=test_data)
    assert resp.status_code == 200
    