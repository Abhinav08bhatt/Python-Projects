from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint

    try:
        response = get(url)
        data = response.json()

        if "results" not in data:
            print("Error: Could not fetch currency list.")
            return []

        currencies = list(data["results"].items())
        currencies.sort()
        return currencies

    except Exception:
        print("Error: API request failed.")
        return []


def print_currencies(currencies):
    if not currencies:
        print("No currencies available.")
        return

    for name, currency in currencies:
        currency_name = currency.get("currencyName", "Unknown")
        _id = currency.get("id", "N/A")
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {currency_name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint

    try:
        data = get(url).json()

        if len(data) == 0:
            print("Invalid currencies.")
            return None

        rate = list(data.values())[0]
        print(f"{currency1} -> {currency2} = {rate}")
        return rate

    except Exception:
        print("Error: Could not retrieve exchange rate.")
        return None


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return None

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return None

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            print("Thank you!")
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()
