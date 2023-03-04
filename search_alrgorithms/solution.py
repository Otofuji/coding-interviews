# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    
    if root is not None:
        # print the value of the current node
        print(root.value)
        # recursively print the left subtree in pre-order
        pre_order_recursive(root.left)
        # recursively print the right subtree in pre-order
        pre_order_recursive(root.right)
    


def pre_order_iterative(root: TreeNode) -> None:
    if root is None:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()
        # print the value of the current node
        print(node.value)
        # push the right child first, so it gets processed after the left child
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def in_order_recursive(root: TreeNode) -> None:
    if root is not None:
        # recursively print the left subtree in in-order
        in_order_recursive(root.left)
        # print the value of the current node
        print(root.value)
        # recursively print the right subtree in in-order
        in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root is not None:
        # recursively print the left subtree in post-order
        post_order_recursive(root.left)
        # recursively print the right subtree in post-order
        post_order_recursive(root.right)
        # print the value of the current node
        print(root.value)


def breadth_first(root: TreeNode) -> None:
    if root is None:
        return
    
    queue = [root]
    front = 0
    rear = 1
    while front < rear:
        # remove the next node from the queue and print its value
        node = queue[front]
        front += 1
        print(node.value)
        # add the left and right children of the current node to the queue (if they exist)
        if node.left is not None:
            queue.append(node.left)
            rear += 1
        if node.right is not None:
            queue.append(node.right)
            rear += 1


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    # Your code goes here

    if node is None:
        return

    visited.add(node)
    print(node.value)
    
    for adjacency in node.adjacent:
        if adjacency not in visited:
            graph_depth_first_recursive(adjacency, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    if not node:
        return
    
    stack = [node]
    visited = set()
    
    while stack:
        no = stack.pop()
        
        if no not in visited:
            visited.add(no)
            print(no.value)
            
            for adjacency in no.adjacent:
                if adjacency not in visited:
                    stack.append(adjacency)

def graph_breadth_first(node: GraphNode) -> None:
    if not node:
        return
    
    queue = [node]
    visited = set()
    
    while queue:
        no = queue.pop(0)
        
        if no not in visited:
            visited.add(no)
            print(no.value)
            
            for adjacency in no.adjacent:
                if adjacency not in visited:
                    queue.append(adjacency)