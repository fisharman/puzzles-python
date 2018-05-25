class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def reverse_ll(root):
    current = root
    next = current
    prev = None

    while next:
        current = next
        next = current.next
        current.next = prev
        prev = current

    return current

"""
1->2->3->null
3->2->1->null
"""

def reverse_ll1(root):
    current = root
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

# reverse linked list in interval
"""
k = 2
1 -> 2 -> 3 -> 4 -> 5
2 -> 1 -> 4 -> 3 -> 5

k = 3
1 -> 2 -> 3 -> 4 -> 5
3 -> 2 -> 1

"""

def merge_sorted(l1: list, l2: list) -> list:
    pass


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    # keep track of the node before m
    # keep track of the node after n
    # reverse list from m to n
    # keep track of m and link it to node after n
    # link node before m to head of list
    # tests
    # case m = n
    # case m = 1, n = len(list)
    # 1 4, 2 5, 1 5

    before_m = None
    current = head
    count = 1

    while count < m:
        before_m = current
        current = current.next
        count += 1

    m_node = current
    prev = None
    for _ in range(m, n + 1):
        next = current.next
        current.next = prev
        prev = current
        current = next

    if prev and before_m:
        before_m.next = prev

    if next:
        m_node.next = next

    if m == 1:
        return prev

    return head


if __name__ == "__main__":
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)


    #root = reverse_ll(root)
    root = reverseBetween(root, 2, 4)
    pass
