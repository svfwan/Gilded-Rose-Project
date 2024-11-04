class QualityManager:
    @staticmethod
    def update_quality(item):
        if item.name.startswith("Conjured"):
            QualityRules.update_conjured(item)
        elif item.name == "Aged Brie":
            QualityRules.update_aged_brie(item)
        elif item.name == "Backstage passes":
            QualityRules.update_backstage_passes(item)
        elif item.name == "Sulfuras":
            QualityRules.update_sulfuras(item)
        else:
            QualityRules.update_normal(item)

class QualityRules:
    @staticmethod
    def update_aged_brie(item):
        item.quality = min(50, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 1)

    @staticmethod
    def update_backstage_passes(item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in <= 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in -= 1

    @staticmethod
    def update_sulfuras(item):
        pass

    @staticmethod
    def update_conjured(item):
        item.quality = max(0, item.quality - 2)
        item.sell_in -= 1

    @staticmethod
    def update_normal(item):
        item.quality = max(0, item.quality - 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 1)
