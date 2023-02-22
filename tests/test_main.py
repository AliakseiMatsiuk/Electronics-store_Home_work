import pytest
from package_name.main import Item


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
    """Тестирует длину имени меньше 10 символов"""
    item = Item("Смартфон", 10000, 20)
    item2 = Item("СуперСмартфон", 10000, 20)
    assert len(item.name) <= 10
    assert len(item2.name) > 10


@pytest.fixture()
def product_name():
    return Item.all


def test_name_length(product_name):
    with pytest.raises(Exception):
        product_name.name = "Длина наименования товара превышает 10 символов."



