class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSymmetry_stack(root):
    if root is None:
        return True

    stack = [(root.left, root.right)]    
    while stack:
        left, right = stack.pop()
        if left is None or right is None:
            return left == right
        elif left.val != right.val:
            return False
        else:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
    return True

def isMirror(left, right):
    if left is None or right is None:
        return left == right
    elif left.val != right.val:
        return False
    
    return isMirror(left.left, right.right) and isMirror(left.right, right.left)

def isSymmetry_recursive(root):
    if root is None:
        return True
    
    return isMirror(root.left, root.right)
    