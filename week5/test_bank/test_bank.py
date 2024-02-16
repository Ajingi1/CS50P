from bank import value

def test_value_start_with_h():
    assert value("how") == 20

def test_value_without_h_init():
    assert value("Today You are good") == 100

def test_value_hello():
    assert value("Hello") == 0
