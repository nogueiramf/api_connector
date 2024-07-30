import os
import requests
import json
from dotenv import load_dotenv
from langchain_core.tools import BaseTool

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class AppInfoFetcherTool(BaseTool):
    """
    Classe que busca informações de um aplicativo da API RankMyApp e salva em um arquivo JSON.

    Atributos:
        name (str): Nome da ferramenta.
        description (str): Descrição da ferramenta.
    """
    name: str = "app_info_fetcher_tool"
    description: str = "Fetches app information from the RankMyApp API and saves it to a JSON file"

    def _run(self) -> str:
        """
        Busca informações do aplicativo e salva em um arquivo JSON.

        Returns:
            str: Mensagem indicando o status da operação.
        """
        api_token = os.getenv('API_TOKEN')
        app_id = os.getenv('APP_ID')

        # Carregar a URL do arquivo .env
        base_url = os.getenv('API_URL')
        if not base_url or not api_token or not app_id:
            return "Environment variables 'API_URL', 'API_TOKEN', or 'APP_ID' not set."

        url = base_url.format(APP_ID=app_id)
        headers = {'rankapi-token': api_token}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            return f"Error fetching data: {e}"
        
        app_data = response.json()

        if 'content' in app_data:
            content = app_data['content']
            title = content.get('title', 'No title available')
            description = content.get('description', 'No description available')
            main_genre = content.get('mainGenre', 'No main genre available')

            app_info = {
                "title": title,
                "description": description,
                "mainGenre": main_genre
            }

            with open('app_info.json', 'w', encoding='utf-8') as json_file:
                json.dump(app_info, json_file, ensure_ascii=False, indent=4)

            return "App information saved to app_info.json"
        else:
            return "Content not found in the response"

# Exemplo de como usar a ferramenta
if __name__ == "__main__":
    tool = AppInfoFetcherTool()
    result = tool._run()
    print(result)
