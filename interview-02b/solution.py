class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def nth_to_last(head: Node, k: int) -> Node:
    if head is None:
        return 0
    i = nth_to_last(head.next, k) + 1
    if i == k:
        
        return i