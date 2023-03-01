import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int, amount: int):
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __repr__(self):
        """Выводим класс"""
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.amount})"

    def __str__(self):
        """Выводим имя"""
        return f"{self.__name}"

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
            raise Exception("Длина наименования товара превышает 10 символов.")

    @staticmethod
    def is_integer(num) -> bool:
        """Определения целого числа в методе класса"""
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        return False

    def __add__(self, other):
        """Слаживаем экземпляры классов"""
        if isinstance(other, Item):
            return self.amount + other.amount


class Phone(Item):

    def __init__(self, name, price, amount, number_of_sim):
        """Наследуем и Добовляем метод number_of_sim"""
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Выводим класс"""
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.amount}, {self.number_of_sim})'

    @property
    def number_of_sim(self):
        return self._sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Деоаем проверку на колличество сим-карт"""
        if value >= 1:
            self._sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# item1 = Item("Смартфон", 10_000, 20)
# phone1.number_of_sim = 2
# print(repr(phone1))
# print(item1 + phone1)
