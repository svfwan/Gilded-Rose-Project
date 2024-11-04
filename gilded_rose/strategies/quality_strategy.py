from abc import ABC, abstractmethod
from gilded_rose.item import Item

class QualityStrategy(ABC):
    @abstractmethod
    def update_quality(self, item: Item):
        pass
