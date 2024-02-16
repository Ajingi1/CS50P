from response import validate



def test_valid():
    assert validate("talle@gmail.com") == "Valid"


def test_invalid_email():
    assert validate("talle@gmail..com") == "Invalid"


def test_empty():
    assert validate("") == "Invalid"
