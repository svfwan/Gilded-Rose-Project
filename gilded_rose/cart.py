from .currency_manager import CurrencyManager
from .discount_manager import DiscountManager

class Cart:
    def __init__(self, currency="USD"):
        self.items = []
        self.currency = currency

    def add_item(self, item):
        self.items.append(item)

    def item_prices(self):
        item_prices = []
        for item in self.items:
            converted_price = CurrencyManager.convert(item.price, item.currency, self.currency)
            item_prices.append((item.name, round(converted_price, 2), self.currency))
        return item_prices

    def total_price(self):
        total = sum(CurrencyManager.convert(item.price, item.currency, self.currency) for item in self.items)
        return round(total, 2)

    def apply_discount(self):
        return DiscountManager.apply_bulk_discount(self)
