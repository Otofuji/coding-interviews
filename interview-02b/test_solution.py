from solution import nth_to_last


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def make_list(l: list) -> list[Node]:
    nodes = [Node(v) for v in l]
    for node, next in zip(nodes[:-1], nodes[1:]):
        node.next = next
    return nodes


def strlist(node: Node) -> str:
    s = []
    while node:
        s.append(str(node.value))
        node = node.next
    return '->'.join(s) or 'Empty'


def check(values: list, k: int):
    head = None
    expected = None
    if values:
        l = make_list(values)
        head = l[0]
        if k <= len(l):
            expected = l[-k]
    ans = nth_to_last(head, k)

    msg = f"Didn't work for list '{strlist(head)}' and k={k}"
    assert expected == ans, msg


def test_1():
    check(None, 10)


def test_2():
    check([1, 1, 1, 1, 1, 1], 3)


def test_3():
    check(range(1, 11), 1)


def test_4():
    check(range(1, 11), 10)


def test_5():
    check(range(1, 11), 20)


def test_6():
    check(range(1, 11), 2)


def test_7():
    check(range(1, 11), 3)


def test_8():
    check(range(1, 11), 4)


def test_9():
    check(range(1, 11), 5)


def test_10():
    check(range(1, 11), 6)
