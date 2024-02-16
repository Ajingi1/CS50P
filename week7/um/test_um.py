from um import count


def test_1_valid():
    assert count("um")  == 1


def test_case_valid():
    assert count("Um.... what are egular expressions make sense now") == 1

def test_multi_valid():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
