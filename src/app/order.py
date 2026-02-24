class Order:
    def __init__(self, items):
        self.items = items  # lista de tuplas (nome, preço, quantidade)

    def total(self):
        total_value = 0
        for name, price, quantity in self.items:
            if price < 0 or quantity < 0:
                raise ValueError("Invalid item data")
            total_value += price * quantity
        return total_value

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount")
        return self.total() * (1 - percent / 100)

    def has_free_shipping(self):
        return self.total() > 200