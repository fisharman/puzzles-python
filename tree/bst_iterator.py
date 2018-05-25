# Calling next() will return the next smallest number in the BST.

# Definition for a binary tree node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        # self.inOrder(root, self.stack)
        current_node = root
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)

    def next(self):
        """
        :rtype: int
        """
        top_node = self.stack.pop()
        current_node = top_node.right
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left

        return top_node.val

    def inOrder(self, root, stack):
        if root is None:
            return

        self.inOrder(root.right, stack)
        self.stack.append(root.val)
        self.inOrder(root.left, stack)


if __name__ == "__main__":
    # Your BSTIterator will be called like this:
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)

    i, v = BSTIterator(root), []

    while i.hasNext():
        v.append(i.next())

    print(v)