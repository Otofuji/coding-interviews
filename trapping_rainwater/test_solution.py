from solution import Solution


def _check(heights, expected):
    ret = Solution().trap(heights)
    assert ret == expected, f'Wrong answer for input {heights}'


def test_1():
    _check([], 0)


def test_2():
    _check([0, 0, 0, 0, 0], 0)


def test_3():
    _check([0, 0, 100, 0, 0], 0)


def test_4():
    _check([10, 0, 100, 0, 10], 20)


def test_5():
    _check([10, 20, 100, 20, 10], 0)


def test_6():
    _check([100, 0, 0, 0, 0], 0)


def test_7():
    _check([0, 0, 0, 0, 10], 0)


def test_8():
    _check([100, 0, 0, 0, 10], 30)


def test_9():
    _check([10, 10, 10, 10, 100], 0)


def test_10():
    _check([20, 100, 0, 10, 0, 100, 10], 290)


def test_11():
    _check([20, 100, 90, 80, 90, 100, 10, 20, 15], 50)


def test_12():
    _check([200, 100, 90, 80, 90, 100, 10, 20, 150], 560)


def test_13():
    _check([199, 200, 100, 90, 80, 90, 100, 10, 20, 150, 142], 560)


def test_14():
    _check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)


def test_15():
    _check([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0)