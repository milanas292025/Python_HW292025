import requests
import pytest


BASE_URL = "<API_BASE_URL>"  # заменить на реальную ссылку API
TOKEN = "<YOUR_AUTH_TOKEN>"  # заменить на настоящий токен авторизации

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {TOKEN}"})
    return session