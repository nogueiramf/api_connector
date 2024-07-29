import os
import requests
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

api_token = os.getenv('API_TOKEN')
app_id = os.getenv('APP_ID')

# Carregar a URL do arquivo .env
base_url = os.getenv('API_URL')
url = base_url.format(APP_ID=app_id)
headers = {'rankapi-token': api_token}

response = requests.get(url, headers=headers)
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

    print(f"Data saved to app_info.json")
else:
    print("Content not found in the response")
