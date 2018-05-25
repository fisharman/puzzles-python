# Definition for a binary tree node
import queue


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []

        if root is None:
            return output

        q = queue.Queue()
        q.put(root)
        while not q.empty():
            nodes = []
            levelNodes = q.qsize()
            for _ in range(levelNodes):
                current_node = q.get()
                nodes.append(current_node.val)
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)
            output.append(nodes)
        return output

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
               :type root: TreeNode
               :rtype: List[List[int]]
               """
        output = []

        if root is None:
            return output

        q = queue.Queue()
        q.put(root)
        while not q.empty():
            nodes = []
            levelNodes = q.qsize()
            for _ in range(levelNodes):
                current_node = q.get()
                nodes.append(current_node.val)
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)
            output.insert(0, nodes)
        return output



if __name__ == "__main__":
    tree1 = TreeNode(3)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.right = TreeNode(4)
    tree1.right.right = TreeNode(5)

    # not valid BST
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
    print(validator.levelOrder(tree3))
    print(validator.levelOrderBottom(tree3))