import requests


API_URL = "https://api.frankfurter.app/latest"

def get_exchange_rate(target_currency: str) -> float:
    response = requests.get(
        API_URL,
        params={
            "from": "BRL",
            "to": target_currency,
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    return data["rates"][target_currency]