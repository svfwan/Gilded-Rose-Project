import unittest
from gilded_rose.item_factory import ItemFactory
from gilded_rose.gilded_rose import GildedRose
from gilded_rose.cart import Cart

class GildedRoseTest(unittest.TestCase):
    def test_item_quality_degrades(self):
        items = [ItemFactory.create_item("Regular Item", 5, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_aged_brie_quality_increases(self):
        items = [ItemFactory.create_item("Aged Brie", 5, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)

    def test_backstage_passes_increase_in_quality(self):
        items = [ItemFactory.create_item("Backstage passes to a concert", 10, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_cart_total_price_in_usd(self):
        cart = Cart(currency="USD")
        cart.add_item(ItemFactory.create_item("Regular Item", 5, 10, 20, "USD"))
        cart.add_item(ItemFactory.create_item("Regular Item", 5, 10, 15, "USD"))
        self.assertEqual(cart.total_price(), 35)

if __name__ == '__main__':
    unittest.main()
