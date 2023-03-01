import pytest
from package_name.main import Item, Phone


def test_init():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.amount == 20


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == item.price * item.amount


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    assert item.apply_discount() == item.price * Item.pay_rate


def test_name():
    item = Item("Смартфон", 10000, 20)
    item.name = 'Телефон'
    assert item.name == 'Телефон'


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.5) == False


def test_name_length_lt_10():
    item = Item('test', 10, 5)
    with pytest.raises(Exception, match="Длина наименования товара превышает 10 символов."):
        item.name = 'This is too long'


@pytest.fixture()
def product_name():
    return Item.all


def test_name_length(product_name):
    with pytest.raises(Exception):
        product_name.name = "Длина наименования товара превышает 10 символов."


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item(Смартфон, 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Смартфон"

def test_phone_init():
    phone = Phone('iPhone', 5000, 1, 3)
    assert phone.name == 'iPhone'
    assert phone.price == 5000
    assert phone.amount == 1
    assert phone.number_of_sim == 3

def test_add():
    item1 = Item('item1', 10, 5)
    item2 = Item('item2', 15, 10)
    result = item1 + item2
    assert result == 15

def test_repr_phone():
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert repr(phone) == "Phone(iPhone 14, 120000, 5, 2)"