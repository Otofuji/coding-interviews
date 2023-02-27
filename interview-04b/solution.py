class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []  # List of Nodes this node points to

def has_route(start_node: GraphNode, end_node: GraphNode) -> bool:
    if start_node == end_node:
        return True

    queue = []
    visited = set()

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        curr_node = queue.pop(0)

        for neighbor in curr_node.adjacent:
            if neighbor == end_node:
                return True

            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return False