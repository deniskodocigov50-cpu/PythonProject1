class Cart:
    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.items:
            return 'Корзина пуста'
        result = 'Корзина:\n'
        for item in self.items:
            result += f'{item['name']}: {item["quantity"]}шт по {item['price']}\n'
        return result
    
    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart

    def add_item(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
