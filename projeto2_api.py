import requests
import pytest

API_URL = "https://api.thecatapi.com/v1/images/search"  
headers = {}

def test_successful_request():
    """Verifica se a API retorna status code 200 para uma requisição válida de gatos."""
    response = requests.get(API_URL, headers=headers)
    assert response.status_code == 200, "A resposta não foi bem-sucedida"
    assert isinstance(response.json(), list), "A resposta não é uma lista de imagens de gatos"

def test_invalid_url():
    """Simula erro ao usar uma URL inválida."""
    invalid_url = "https://api.thecatapi.com/v1/invalid_endpoint"
    response = requests.get(invalid_url, headers=headers)
    assert response.status_code == 404, "Status code não é 404 para URL inválida"

def test_validate_data():
    """Valida que a resposta contém informações sobre o gato."""
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    # Verifica se o dado contém a chave 'url' que indica a imagem do gato
    assert "url" in data[0], "A chave 'url' não está na resposta"
    assert isinstance(data[0]["url"], str), "A 'url' não é uma string"

