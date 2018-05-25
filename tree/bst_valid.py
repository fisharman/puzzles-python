# Definition for a binary tree node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #return self.valid_bst_recursive(root)
        return self.valid_bst_iterative(root)

    def valid_bst_recursive(self, root, mini=float('-inf'), maxi=float('inf')):
        """
        :type root: TreeNode
        :type mini: int
        :type maxi: int
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= mini or root.val >= maxi:
            return False
        return self.valid_bst_recursive(root.left,mini,root.val) and self.valid_bst_recursive(root.right,root.val,maxi)

    def valid_bst_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # traverse through using stack
        if root is None:
            return True

        before_val = float('-inf')
        stack = []
        current_node = root

        while current_node or len(stack) > 0:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            if current_node.val <= before_val:
                return False
            before_val = current_node.val
            current_node = current_node.right

        return True


if __name__ == "__main__":
    tree1 = TreeNode(3)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.right = TreeNode(4)
    tree1.right.right = TreeNode(5)

    tree2 = TreeNode(3)
    tree2.left = TreeNode(5)
    tree2.right = TreeNode(6)

    tree3 = TreeNode(8)
    tree3.left = TreeNode(4)
    tree3.left.left = TreeNode(2)
    tree3.left.left.left = TreeNode(1)
    tree3.left.left.right = TreeNode(3)
    tree3.left.right = TreeNode(6)
    tree3.left.right.left = TreeNode(5)
    tree3.left.right.right = TreeNode(7)

    # not valid BST
    tree4 = TreeNode(8)
    tree4.left = TreeNode(4)
    tree4.left.left = TreeNode(2)
    tree4.left.left.left = TreeNode(1)
    tree4.left.left.right = TreeNode(3)
    tree4.left.right = TreeNode(6)
    tree4.left.right.left = TreeNode(7)
    tree4.left.right.right = TreeNode(5)

    validator = Solution()
    print(validator.isValidBST(tree3))
