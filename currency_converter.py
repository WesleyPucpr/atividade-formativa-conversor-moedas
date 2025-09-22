import requests

API_URL = "https://open.er-api.com/v6/latest/"  # API gratuita para câmbio

def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Converte um valor de uma moeda para outra usando a API open.er-api.com.
    Retorna uma string formatada com o resultado ou mensagem de erro.
    """
    try:
        response = requests.get(f"{API_URL}{from_currency.upper()}")
        data = response.json()

        if response.status_code != 200 or data.get("result") != "success":
            return f"Error fetching exchange rates for {from_currency.upper()}"

        rates = data.get("rates", {})
        if to_currency.upper() not in rates:
            return f"Currency {to_currency.upper()} not found"

        converted = amount * rates[to_currency.upper()]
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"

    except Exception as e:
        return f"Error fetching exchange rates: {str(e)}"


def get_available_currencies() -> list:
    """
    Retorna a lista de moedas disponíveis na API.
    """
    try:
        response = requests.get(f"{API_URL}USD")
        data = response.json()

        if response.status_code != 200 or data.get("result") != "success":
            return []

        return list(data.get("rates", {}).keys())

    except Exception:
        return []
