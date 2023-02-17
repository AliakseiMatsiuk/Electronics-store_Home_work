class Item:
    pay_rate = 0.8
    instances = []

    def __init__(self, name: str, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        Item.instances.append(self)

    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        return self.pay_rate * self.price

# item1 = Item("Смартфон", 10000, 20)
# item2 = Item("Ноутбук", 20000, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())