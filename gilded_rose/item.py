class Item:
    def __init__(self, name, sell_in, quality, price, currency="USD", strategy=None):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.price = price
        self.currency = currency
        self.strategy = strategy

    def update_quality(self):
        if self.strategy:
            self.strategy.update_quality(self)

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}, {self.price} {self.currency}"
