import pytest
from fuel import convert, gauge


def test_perc():
   assert gauge(1)  == "E"
def test_percen():
   assert gauge(10) == f"{10}%"
def test_full():
   assert gauge(99) == "F"

def test_int():
   convert(1/2) == 50
   convert(99/100) == 99
   convert(1/100) == 1


def test_int():
   with pytest.raises(ValueError):
      convert("2/1")


def test_zero():
   with pytest.raises(ZeroDivisionError):
      convert("1/0")
