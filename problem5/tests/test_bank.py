from bank import value

def test_hello():
    assert value("Hello") == 0

def test_h_word():
    assert value("hotdog") == 20

def test_not_h():
    assert value("What's up") == 100
