from .quality_strategy import QualityStrategy

class ConjuredItemStrategy(QualityStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        if item.quality < 0:
            item.quality = 0
