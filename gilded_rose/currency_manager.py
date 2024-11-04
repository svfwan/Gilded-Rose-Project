class CurrencyManager:
    exchange_rates = {"USD": 1, "EUR": 0.85, "JPY": 110}

    @staticmethod
    def convert(price, from_currency, to_currency):
        return price * CurrencyManager.exchange_rates[to_currency] / CurrencyManager.exchange_rates[from_currency]
