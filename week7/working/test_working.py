from working import convert
import pytest


def test_without_minute():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_minute():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("cat")

def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("13:60 AM to 28:30 PM")
