from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_inValid_with_0():
    assert is_valid("CS05") == False

def test_inValid_number_in_middle():
    assert is_valid("CS50P") == False

def test_inVali_leng():
    assert is_valid("PI3.14") == False

def test_length():
    assert is_valid("CSCSCS50") == False

def test_start_with_number():
    assert is_valid("1GCS") == False

def test_all_string():
    assert is_valid("CSCS") == True

def tes_empty():
    assert is_valid("56Cs") == False
    assert is_valid("5") == False
    assert is_valid("5Cs") == False
    assert is_valid("C5") == False
