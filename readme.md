# Testes de 5 APIs

Este repositório contém testes para cinco APIs populares: **OpenWeatherMap**, 
**Cat Facts**, **The Dog API**, **JokeAPI**, e **CoinGecko**. 
- Os testes são implementados utilizando a biblioteca pytest 
para garantir o funcionamento correto das APIs.

# Descrição das APIs

### 1. OpenWeatherMap API (Clima e Meteorologia)
A **OpenWeatherMap API** fornece dados sobre o clima, como temperatura,
 umidade, previsão e condições meteorológicas. Para este projeto, realizamos
  testes para verificar as condições climáticas da cidade de Manaus.

### 2. Cat Facts API (Fatos sobre Gatos)
A **Cat Facts API** fornece fatos aleatórios sobre gatos. Esses dados podem ser 
interessantes para os amantes de gatos que buscam informações sobre esses felinos.

### 3. The Dog API (Raças de cães)
A **The Dog API** retorna informações sobre diferentes raças de cães, incluindo imagens, 
características e origens. O objetivo dos testes é garantir que a API retorne informações
 corretas sobre as raças de cães.

### 4. JokeAPI (Piadas Aleatórias)
A **JokeAPI** gera piadas aleatórias em várias categorias, como programação, geral, etc.
 Realizamos testes para garantir que as piadas são retornadas conforme esperado.

### 5. CoinGecko API (Preços de Criptomoedas)
A **CoinGecko API** oferece informações sobre preços e mercado de criptomoedas em tempo real. 
Os testes verificam se os preços das criptomoedas estão sendo retornados corretamente.

## Requisitos Solicitados 

- Python
- pytest

# Como Rodar os Testes

- Passo: Instalar as dependências

Certifiquei de que o pip está atualizado e instalei as dependências necessárias:

## 1. pip install -r requirements.txt


# requirements.txt

Este arquivo contém as bibliotecas necessárias para o projeto,
 como pytest e requests

# Estrutura de Arquivos

- projeto1_api.py: Arquivo com os testes para a OpenWeatherMap API.
- projeto2_api.py: Arquivo com os testes para a Cat Facts API.
- projeto3_api.py: Arquivo com os testes para a The Dog API.
- projeto4_api.py: Arquivo com os testes para a JokeAPI.
- projeto5_api.py: Arquivo com os testes para a CoinGecko API.
- requirements.txt: Arquivo com as dependências necessárias.

# Estrutura Geral de Testes

- Bibliotecas Utilizadas:

## 1. pytest: Framework para execução de testes.
## 2. requests: Biblioteca para realizar requisições HTTP.

- Tipos de Testes:

## 1. Status Code: Confirma que o retorno HTTP está correto.
## 2. Estrutura de Dados: Valida JSON, listas, dicionários e tipos específicos.
## 3. Cenários Negativos: Garante tratamento adequado para erros.