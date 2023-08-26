from fastapi.testclient import TestClient

from main import app


def test_root_get():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()

def test_query_limit():
    with TestClient(app) as client:
        response = client.get("/query?limit=1")
        assert response.status_code == 200
        assert response.json() == {"results":[{"date":"2012-01-01","precipitation":0.0,"temp_max":12.8,"temp_min":5.0,"wind":4.7,"weather":"drizzle"}]}

def test_query_limit_with_weather():
    with TestClient(app) as client:
        response = client.get("/query?limit=1&weather=rain")
        assert response.status_code == 200
        assert response.json() == {"results":[{"date":"2012-01-02","precipitation":10.9,"temp_max":10.6,"temp_min":2.8,"wind":4.5,"weather":"rain"}]}

def test_query_limit_with_weather_and_date():
    with TestClient(app) as client:
        response = client.get("/query?limit=1&weather=rain&date=2012-01-03")
        assert response.status_code == 200
        assert response.json() == {"results":[{"date":"2012-01-03","precipitation":0.8,"temp_max":11.7,"temp_min":7.2,"wind":2.3,"weather":"rain"}]}