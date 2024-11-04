from gilded_rose.item import Item
from gilded_rose.strategies.normal_strategy import NormalItemStrategy
from gilded_rose.strategies.aged_brie_strategy import AgedBrieStrategy
from gilded_rose.strategies.backstage_passes_strategy import BackstagePassesStrategy
from gilded_rose.strategies.conjured_strategy import ConjuredItemStrategy

class ItemFactory:
    @staticmethod
    def create_item(name, sell_in, quality, price, currency="USD"):
        if name == "Aged Brie":
            strategy = AgedBrieStrategy()
        elif name.startswith("Backstage passes"):
            strategy = BackstagePassesStrategy()
        elif name.startswith("Conjured"):
            strategy = ConjuredItemStrategy()
        else:
            strategy = NormalItemStrategy()
        
        return Item(name, sell_in, quality, price, currency, strategy=strategy)
