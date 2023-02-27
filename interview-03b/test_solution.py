from solution import Stack, sort_stack


def _check(values):
    stack = Stack()
    stack._items = [v for v in values]
    sort_stack(stack)

    msg = "Didn't work for the stack: {values}"
    assert stack._items == sorted(values, reverse=True), msg


def test_1():
    _check([])


def test_2():
    _check([1])


def test_3():
    _check(list(range(1, 11)))


def test_4():
    _check(list(range(10, 0, -1)))


def test_5():
    values = []
    for i in range(1, 11):
        values.append(i)
        values.append(10-i+1)
    _check(values)


def test_6():
    values = []
    for i in range(1, 11):
        for _ in range(5):
            values.append(i)
        for _ in range(5):
            values.append(10-i+1)
    _check(values)


def test_7():
    _check([1, 1, 1, 1, 1, 1, 1])


def test_8():
    _check([-1, -1, -1, -1, -1, -1, -1])


def test_9():
    values = []
    for i in range(1, 11):
        values.append(-(10-i+1))
        values.append(-i)
    _check(values)


def test_10():
    values = []
    for i in range(1, 11):
        for _ in range(5):
            values.append(-(10-i+1))
        for _ in range(5):
            values.append(-i)
    _check(values)
