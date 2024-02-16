from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
def test_validate_multiple():
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("8.8.8") == False

def test_5_number():
    assert validate("10.10.10.10.10") == False

def test_validate_invalid():
    assert validate("256.255.255.255") == False

def test_first_range():
    assert validate("255.267.400.900") == False

