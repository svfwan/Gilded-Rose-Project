from .quality_strategy import QualityStrategy

class NormalItemStrategy(QualityStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
