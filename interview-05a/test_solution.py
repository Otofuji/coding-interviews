from solution import longest_sequence


def _check(n_bin, expected):
    n = int(n_bin, base=2)
    received = longest_sequence(n)

    msg = f'Wrong answer for input {n}. Expected: {expected}. Got: {received}.'
    assert expected == received, msg


def test_1():
    _check('00000000000000000000000000000000', 1)


def test_2():
    _check('00000000000000000100000000000000', 2)


def test_3():
    _check('11111111111111111101111111111111', 32)


def test_4():
    _check('11111111111111111111111111111110', 32)


def test_5():
    _check('10011001110011110011111001111001', 6)


def test_6():
    _check('10110111011110011111001010101010', 8)


def test_7():
    _check('10101010101010101010101010101010', 3)


def test_8():
    _check('10110111011110111110111111011111', 12)


def test_9():
    _check('11001100110011001100110010110011', 4)


def test_10():
    _check('00010111111111111111111111101000', 24)
