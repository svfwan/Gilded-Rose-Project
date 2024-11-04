from .quality_strategy import QualityStrategy

class BackstagePassesStrategy(QualityStrategy):
    def update_quality(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0
        item.sell_in -= 1
        if item.quality > 50:
            item.quality = 50
