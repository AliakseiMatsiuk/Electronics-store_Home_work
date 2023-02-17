from package_name.main import Item

def test_init():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.amount == 20

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == item1.price * item1.amount

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.apply_discount() == item1.price * Item.pay_rate