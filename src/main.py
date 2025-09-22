import requests


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if 'rates' not in data:
            return "Error: Invalid API response"

        rate = data['rates'].get(to_currency)
        if not rate:
            return f"Currency {to_currency} not found"

        converted_amount = amount * rate
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    except requests.RequestException as e:
        return f"Error fetching exchange rates: {e}"


def get_available_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return list(data['rates'].keys())
    except requests.RequestException:
        return ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR", "BRL"]


def main():
    currencies = get_available_currencies()
    if not currencies:
        print("Unable to fetch currencies")
        return

    print("Available currencies:", ", ".join(currencies))

    try:
        amount = float(input("Enter amount to convert: "))
        from_currency = input("Enter source currency (e.g., USD): ").upper()
        to_currency = input("Enter target currency (e.g., EUR): ").upper()

        if from_currency not in currencies or to_currency not in currencies:
            print("Invalid currency code")
            return

        result = convert_currency(amount, from_currency, to_currency)
        print(result)

    except ValueError:
        print("Invalid amount entered")


if __name__ == "__main__":
    main()