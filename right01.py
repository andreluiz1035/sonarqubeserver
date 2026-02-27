import requests

TOKEN = os.getenv("KICKAPI_TOKEN")
if not TOKEN:
    raise RuntimeError("Defina a env var KICKAPI_TOKEN")

# URL da API
URL = "https://kickapi.com.br/token"

# Headers com autenticação
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

try:
    response = requests.get(URL, headers=headers, timeout=30)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Resposta JSON:")
        print(response.json())
    else:
        print("Erro:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", str(e))