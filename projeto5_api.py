import requests
import pytest

# URL base da CoinGecko API
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Definir as criptomoedas de interesse, citei exemplos, Bitcoin (btc) e Ethereum (eth)
CRYPTOCURRENCIES = ["bitcoin", "ethereum"]

def test_successful_request():
    """Verifica se a API retorna status code 200 para uma requisição válida."""
    params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}  # Parâmetros para as moedas e moedas fiduciárias
    response = requests.get(API_URL, params=params)
    assert response.status_code == 200, "A requisição não retornou status code 200"
    data = response.json()
    assert "bitcoin" in data, "Bitcoin não encontrado na resposta"
    assert "ethereum" in data, "Ethereum não encontrado na resposta"
    assert "usd" in data["bitcoin"], "Preço de Bitcoin em USD não encontrado"
    assert "usd" in data["ethereum"], "Preço de Ethereum em USD não encontrado"

def test_invalid_url():
    """Simula erro ao usar uma URL inválida."""
    invalid_url = "https://api.coingecko.com/api/v3/simple/invalid_endpoint"
    response = requests.get(invalid_url)
    assert response.status_code == 404, "Status code não é 404 para URL inválida"

def test_invalid_parameters():
    """Simula erro ao passar parâmetros inválidos na requisição."""
    params = {"ids": "invalidcryptocurrency", "vs_currencies": "usd"}
    response = requests.get(API_URL, params=params)
    
    # Verifica se o status code ainda é 200
    assert response.status_code == 200, "Status code não é 200 para parâmetros inválidos"
    
    # Verifica se a resposta está vazia ou não contém dados para a criptomoeda inválida
    data = response.json()
    assert "invalidcryptocurrency" not in data, "A resposta contém dados para uma criptomoeda inválida"
    assert data == {}, "A resposta não deve conter dados válidos"

def test_validate_crypto_data():
    """Verifica se os dados da criptomoeda (preço em USD) são retornados corretamente."""
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    response = requests.get(API_URL, params=params)
    data = response.json()
    assert "bitcoin" in data, "Bitcoin não encontrado na resposta"
    # Modificado para verificar se o valor é um número positivo (inteiro ou flutuante)
    assert isinstance(data["bitcoin"]["usd"], (int, float)), "O preço de Bitcoin não é numérico"
    assert data["bitcoin"]["usd"] > 0, "O preço de Bitcoin deve ser maior que 0"
