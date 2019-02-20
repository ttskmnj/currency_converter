from urllib.request import urlopen
import json


class CurrencyConverter:
    url = "https://api.exchangeratesapi.io/latest?"
    currency_code = ["ISK", "CAD", "MXN", "CHF", "AUD", "CNY", "GBP", "USD", "SEK", "NOK", "TRY", "IDR", "ZAR", "HRK",
                     "EUR", "HKD", "ILS", "NZD", "MYR", "JPY", "CZK", "SGD", "RUB", "RON", "HUF", "BGN", "INR", "KRW",
                     "DKK", "THB", "PHP", "PLN", "BRL"]
    currency_symbol = {"£": "GBP", "$": "USD", "Rp": "IDR", "R": "ZAR", "kn": "HRK", "€": "EUR", "₪": "ILS",
                       "RM": "MYR", "Kč": "CZK", "₽": "RUB", "lei": "RON", "Ft": "HUF", "лв": "BGN", "₩": "KRW",
                       "฿": "THB", "zł": "PLN", "R$": "BRL"}

    ##########################
    # get rates from web API #
    ##########################
    @classmethod
    def get_rates(cls, base, symbol):
        base_par = "base=" + base
        symbol_par = "&symbols=" + symbol if symbol else ""

        with urlopen(cls.url + base_par + symbol_par) as response:
            # convert json to dictionary
            result = json.loads(response.read().decode('utf8'))

        return result

    ##############################
    # generate results to output #
    ##############################
    @classmethod
    def generate_results(cls, amount, rates):
        output = {}

        for k, v in rates['rates'].items():
            output[k] = float("{0:.2f}".format(v * amount))

        results = {
            "input": {
                "amount": amount,
                "currency": rates['base']
            },
            "output": output
        }

        return results
