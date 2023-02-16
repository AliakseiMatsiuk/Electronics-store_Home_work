class Item:
    pay_rate = 0.8
    instances = []

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        Item.instances.append(self)

    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        return self.pay_rate * self.price

