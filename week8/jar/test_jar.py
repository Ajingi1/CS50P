from jar import Jar
import pytest


def test_init():
    jar = Jar(11)
    assert jar.capacity == 11
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_invalid_deposit():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(20)

def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6

def test_invalid_withdraw():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(3)
        jar.withdraw(5)
