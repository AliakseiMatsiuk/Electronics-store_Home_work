import csv
class Item:
    pay_rate = 0.8
    all = []

    def __init__(self,name:str,price:int,amount:int):
        self.__name = name
        self.price = price
        self.amount = amount
        Item.all.append(self)

    def calculate_total_price(self):
        """Возвращает цену товра"""
        return self.price * self.amount

    def apply_discount(self):
        """Применяет к цене скидку"""
        return self.pay_rate * self.price

    @classmethod
    def instantiate_from_csv(cls):
        """Создаёт новые экзэмпляры из csv файла"""
        with open("items.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @property
    def name(self):
        """Возвращает название товра"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Контролирует длину названия товра"""
        if len(value) <= 10:
            self.__name = value
        else:
            print(f'Exception: Длина наименования товара превышает 10 символов.')

    @staticmethod
    def is_integer(num) -> bool:
        """Определения целого числа в методе класса"""
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        return False


#item = Item("Смартфон", 10000, 20)
# Item.instantiate_from_csv()
# print(len(Item.all))
# i = Item.all[0]
#print(Item.is_integer(5.5))