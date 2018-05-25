class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node


def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not

    if root is None:
        return 0

    if root.value == val:
        return 1

    if val > root.value:
        return isPresent(root.right, val)
    else:
        return isPresent(root.left, val)




if __name__ == "__main__":
    _a = None
    _a_size = int(input())
    _a_i = 0

    while _a_i < _a_size:
        _a_item = int(input())
        _a = _insert_node_into_binarysearchtree(_a, _a_item)
        _a_i += 1

    q = int(input())
    i = 0

    while i < q:
        _b = int(input())
        _result = isPresent(_a, _b);
        print(_result)
        i += 1