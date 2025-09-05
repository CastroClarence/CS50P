from plates import is_valid

def test_special():
    assert is_valid("CST50.") == False

def test_first_two():
    assert is_valid("50CST") == False

def test_number():
    assert is_valid("CS50T") == False

def test_allnum():
    assert is_valid("504234") == False

def test_len():
    assert is_valid("A") == False

def test_mid():
    assert is_valid("CS05") == False
