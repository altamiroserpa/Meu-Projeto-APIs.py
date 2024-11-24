import requests
import pytest

# URL base da JokeAPI para obter piadas aleatórias
API_URL = "https://v2.jokeapi.dev/joke/Any"
headers = {}

def test_successful_request():
    """Verifica se a API retorna status code 200 para uma requisição válida de piadas."""
    response = requests.get(API_URL, headers=headers)
    assert response.status_code == 200, "A resposta não foi bem-sucedida"
    assert "joke" in response.json() or "setup" in response.json(), "A resposta não contém uma piada válida"

def test_invalid_url():
    """Simula erro ao usar uma URL inválida."""
    invalid_url = "https://v2.jokeapi.dev/joke/invalid_endpoint"
    response = requests.get(invalid_url, headers=headers)
    assert response.status_code == 400, "Status code não é 400 para URL inválida"  # Alterado de 404 para 400

def test_invalid_category():
    """Simula erro ao solicitar piadas de uma categoria inválida."""
    invalid_category_url = "https://v2.jokeapi.dev/joke/invalidcategory"
    response = requests.get(invalid_category_url, headers=headers)
    assert response.status_code == 400, "Status code não é 400 para categoria inválida"  # Alterado de 404 para 400

def test_validate_joke_data():
    """Valida se a resposta contém dados corretos para a piada."""
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    # Verifica se a resposta contém a chave 'joke' ou 'setup'
    assert "joke" in data or "setup" in data, "A resposta não contém a chave 'joke' ou 'setup'"
    
    # Se a piada for dividida em 'setup' e 'delivery', valida ambos
    if "setup" in data and "delivery" in data:
        assert isinstance(data["setup"], str), "O 'setup' não é uma string"
        assert isinstance(data["delivery"], str), "O 'delivery' não é uma string"
    else:
        assert isinstance(data["joke"], str), "A piada não é uma string"

def test_programming_category():
    """Verifica piadas da categoria 'Programming'."""
    programming_url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(programming_url, headers=headers)
    assert response.status_code == 200, "A resposta para a categoria 'Programming' não foi bem-sucedida"
    assert "joke" in response.json() or "setup" in response.json(), "A resposta não contém uma piada de programação válida"
