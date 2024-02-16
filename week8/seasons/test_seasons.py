from seasons import get_dif, Validate_date, convert_to_minutes, convert_to_words
import pytest


def test_validate():
    with pytest.raises(SystemExit) as excinfo:
        Validate_date("2000/02/30")
        assert excinfo.value.code == 1
# def test_on_years():
#     assert get_dif("2023-02-14") == 365
# def test_two_years():
#     assert get_dif("2022-02-14") == 730
def test_min():
    assert convert_to_minutes(365) == 525600
def test_word_converter():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
