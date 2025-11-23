import pytest
from utils import generate_random_project_data

PROJECT_ID = None  # будет храниться ID проекта, созданного в тестах

def create_project(api_client):
    global PROJECT_ID
    payload = generate_random_project_data()
    response = api_client.post(f"{BASE_URL}/api-v2/projects", json=payload)
    assert response.status_code == 201
    PROJECT_ID = response.json()['id']

def update_project(api_client):
    new_payload = {"title": "Updated Title"}
    response = api_client.put(f"{BASE_URL}/api-v2/projects/{PROJECT_ID}", json=new_payload)
    assert response.status_code == 200
    assert response.json()['title'] == new_payload['title']

def get_project(api_client):
    response = api_client.get(f"{BASE_URL}/api-v2/projects/{PROJECT_ID}")
    assert response.status_code == 200
    assert response.json()['title'] == "Updated Title"

def delete_project(api_client):
    response = api_client.delete(f"{BASE_URL}/api-v2/projects/{PROJECT_ID}")
    assert response.status_code == 204

# Positive tests
def test_create_project_positive(api_client):
    create_project(api_client)

def test_update_project_positive(api_client):
    update_project(api_client)

def test_get_project_positive(api_client):
    get_project(api_client)

# Negative tests
def test_create_project_negative_missing_required_field(api_client):
    payload = {}  # пустой словарь
    response = api_client.post(f"{BASE_URL}/api-v2/projects", json=payload)
    assert response.status_code == 400 or response.status_code == 422  # зависимо от требований API

def test_update_project_negative_wrong_type(api_client):
    wrong_payload = {"title": 123}  # неверный тип данных
    response = api_client.put(f"{BASE_URL}/api-v2/projects/{PROJECT_ID}", json=wrong_payload)
    assert response.status_code == 400 or response.status_code == 422

def test_get_nonexistent_project(api_client):
    non_existent_id = 999999  # заведомо несуществующий ID
    response = api_client.get(f"{BASE_URL}/api-v2/projects/{non_existent_id}")
    assert response.status_code == 404