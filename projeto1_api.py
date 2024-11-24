import requests  
from unittest.mock import patch  # Import foi necessário para usar mocks

# URL da API
API_URL = "http://api.openweathermap.org/data/2.5/weather"

# Simulações para os testes
MOCK_SUCCESS_RESPONSE = {
    "weather": [{"description": "clear sky"}],
    "main": {"temp": 30.5, "humidity": 70},
    "name": "Manaus",
}

MOCK_ERROR_RESPONSE = {"cod": 404, "message": "city not found"}

@patch("requests.get")
def test_successful_request(mock_get):
    """Testa uma requisição bem-sucedida usando mock."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCK_SUCCESS_RESPONSE

    response = requests.get(API_URL)
    assert response.status_code == 200
    assert "weather" in response.json()
    assert "main" in response.json()

@patch("requests.get")
def test_invalid_city(mock_get):
    """Testa uma cidade inválida usando mock."""
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = MOCK_ERROR_RESPONSE

    response = requests.get(API_URL)
    assert response.status_code == 404
    assert response.json().get("message") == "city not found"
