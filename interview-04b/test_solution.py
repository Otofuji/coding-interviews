from collections import deque
from solution import GraphNode, has_route


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: Adjacency matrix (must be square)
        '''
        self.adj_matrix = adjacency
        n = len(adjacency)
        self.nodes = [GraphNode(i) for i in range(n)]
        for i, node in enumerate(self.nodes):
            node.adjacent = [self.nodes[j] for j, is_adjacent in enumerate(adjacency[i]) if is_adjacent and node != self.nodes[j]]

    def __str__(self):
        return str(self.adj_matrix)


def ground_truth(adj, origin, dst):
    n = len(adj)
    visited = [False for _ in range(n)]
    q = deque([origin])
    while q:
        i = q.popleft()
        for j in range(n):
            if not adj[i][j]:
                continue
            if j == dst:
                return True
            if not visited[j]:
                visited[j] = True
                q.append(j)
    return False


def _check(adj_mat):
    g = Graph(adj_mat)
    for i, origin in enumerate(g.nodes):
        for j, dst in enumerate(g.nodes):
            expected = ground_truth(adj_mat, i, j)
            received = has_route(origin, dst)
            assert expected == received, f"Didn't work for graph:\n{g}"


def test_1():
    _check([[1]])


def test_2():
    _check([
        [1, 0],
        [0, 1],
    ])


def test_3():
    _check([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ])


def test_4():
    _check([
        [1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1],
    ])


def test_5():
    _check([
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ])
