# App API Connector

Este projeto é uma ferramenta simples que busca informações sobre aplicativos usando a API do RankMyApp e salva esses dados em um arquivo JSON.

## Tecnologias Utilizadas

- Python
- Requests
- Dotenv
- langchain-core

## Pré-requisitos

Antes de executar o projeto, você precisa ter o Python e o `pip` instalados em sua máquina. Além disso, certifique-se de ter um arquivo `.env` configurado com as seguintes variáveis:

API_TOKEN=<seu_token_aqui>
APP_ID=<seu_app_id_aqui>
API_URL=<sua_url_aqui>


Substitua `<seu_token_aqui>` e `<seu_app_id_aqui>` pelos valores apropriados.

## Instalação

1. Clone o repositório:

    ```bash
    git clone <url_do_repositorio>
    cd <nome_do_repositorio>
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

    Para ativar o ambiente virtual:

    - No Linux ou macOS:
    
        ```bash
        source venv/bin/activate
        ```

    - No Windows:
    
        ```bash
        venv\Scripts\activate
        ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Certifique-se de que o arquivo `.env` está configurado corretamente.

2. Execute o script:

    ```bash
    python api_connector.py
    ```

3. Os dados do aplicativo serão salvos em um arquivo chamado `app_info.json`.
