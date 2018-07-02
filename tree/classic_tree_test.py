import pytest
from classic_tree import TreeNode, isSymmetry_stack, isSymmetry_recursive

@pytest.fixture(scope='function')
def setup_tree_true():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right = TreeNode(2)
    tree.right.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    return tree

@pytest.fixture(scope='function')
def setup_tree_false():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(2)
    tree.right.right = TreeNode(3)
    return tree

@pytest.fixture(scope='function')
def setup_tree_false1():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    return tree


def test_isSymmetry_stack():
    assert isSymmetry_stack(setup_tree_true())    
    assert not isSymmetry_stack(setup_tree_false())
    assert not isSymmetry_stack(setup_tree_false1())
    
def test_isSymmetry_recursive():
    assert isSymmetry_recursive(setup_tree_true())    
    assert not isSymmetry_recursive(setup_tree_false())
    assert not isSymmetry_recursive(setup_tree_false1())