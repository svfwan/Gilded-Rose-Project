from gilded_rose.item_factory import ItemFactory
from gilded_rose.gilded_rose import GildedRose
from gilded_rose.cart import Cart
from gilded_rose.currency_manager import CurrencyManager
from tabulate import tabulate

def display_menu():
    print("\n===== Gilded Rose Inventory Management =====")
    print("1. Update item quality")
    print("2. View items in inventory")
    print("3. View individual item prices in cart")
    print("4. View total cart price")
    print("5. Change cart currency")
    print("6. Exit")
    print("============================================")

def main():
    items = [
        ItemFactory.create_item("Aged Brie", 10, 20, 30),
        ItemFactory.create_item("Backstage passes to a concert", 5, 10, 50),
        ItemFactory.create_item("Sulfuras, Hand of Ragnaros", 0, 80, 100),
        ItemFactory.create_item("Conjured Mana Cake", 3, 6, 20),
        ItemFactory.create_item("Regular Item", 5, 10, 15)
    ]

    gilded_rose = GildedRose(items)
    cart = Cart(currency="USD")

    for item in items:
        cart.add_item(item)

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            gilded_rose.update_quality()
            print("Quality updated for all items.")
        
        elif choice == "2":
            print("\n===== Items in Inventory =====")
            headers = ["Name", "SellIn", "Quality", "Price"]
            table_data = [
                [
                    item.name, 
                    item.sell_in, 
                    item.quality, 
                    f"{CurrencyManager.convert(item.price, item.currency, cart.currency)} {cart.currency}"
                ]
                for item in items
            ]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        elif choice == "3":
            print("\n===== Individual Item Prices in Cart =====")
            headers = ["Name", "Price", "Currency"]
            table_data = [
                [name, price, currency]
                for name, price, currency in cart.item_prices()
            ]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        elif choice == "4":
            print(f"Total price in {cart.currency}: {cart.total_price()} {cart.currency}")
        
        elif choice == "5":
            print("\nAvailable currencies: USD, EUR, JPY")
            new_currency = input("Enter new currency: ").upper()
            if new_currency in CurrencyManager.exchange_rates:
                cart.currency = new_currency
                print(f"Currency changed to {new_currency}.")
            else:
                print("Invalid currency. Please try again.")
        
        elif choice == "6":
            print("Exiting Gilded Rose Inventory Management.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
