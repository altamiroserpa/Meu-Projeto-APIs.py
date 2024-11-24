import requests
import pytest

API_URL = "https://dog.ceo/api/breeds/list/all"  # raças de cães
headers = {}

def test_successful_request():
    """Verifica se a API retorna status code 200 para uma requisição válida de raças de cães."""
    response = requests.get(API_URL, headers=headers)
    assert response.status_code == 200, "A resposta não foi bem-sucedida"
    assert isinstance(response.json(), dict), "A resposta não é um dicionário de raças de cães"

def test_invalid_url():
    """Simula erro ao usar uma URL inválida."""
    invalid_url = "https://dog.ceo/api/invalid_endpoint"
    response = requests.get(invalid_url, headers=headers)
    assert response.status_code == 404, "Status code não é 404 para URL inválida"

def test_validate_breeds_data():
    """Valida que a resposta contém dados corretos sobre as raças de cães."""
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    # Verifica se a resposta contém um dicionário de raças
    assert "message" in data, "A resposta não contém a chave 'message'"
    assert isinstance(data["message"], dict), "A chave 'message' não contém um dicionário de raças"
    
    # Verifica se pelo menos uma raça está presente
    assert len(data["message"]) > 0, "A resposta não contém raças"

def test_invalid_breed_request():
    """Simula erro ao solicitar imagens de uma raça inexistente."""
    invalid_breed_url = "https://dog.ceo/api/breed/invalidbreed/images"
    response = requests.get(invalid_breed_url, headers=headers)
    assert response.status_code == 404, "Status code não é 404 para raça inválida"
