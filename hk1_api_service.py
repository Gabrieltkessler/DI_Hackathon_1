import requests

def get_exchange_rate(base="USD", target="EUR"):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"

    response = requests.get(url)
    data = response.json()

    if "rates" in data:
        return data["rates"][target]
    else:
        return None