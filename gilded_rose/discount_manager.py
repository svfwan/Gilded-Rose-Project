class DiscountManager:
    @staticmethod
    def apply_bulk_discount(cart, threshold=5, discount=0.10):
        if len(cart.items) >= threshold:
            return cart.total_price() * (1 - discount)
        return cart.total_price()
