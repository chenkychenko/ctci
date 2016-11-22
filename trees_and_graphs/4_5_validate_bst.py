# 4.5 Validate BST
# ==============================================================================================
# Implement a function to check if a binary tree is a binary search tree
# ==============================================================================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque
import sys
def print_tree(node):
    queue = deque([])
    queue.append(node)
    while queue:
        cur_node = queue.popleft()
        print cur_node.data
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

last_visited = None
def validate_in_order(node):
    """
    **In order traversal does not work if there are duplicates** If there are no duplicates
    we can use this function.
    """
    global last_visited
    if not node:
        return True
    if not validate_in_order(node.left):
        return False
    if last_visited and last_visited > node.data:
        return False
    last_visited = node.data
    if not validate_in_order(node.right):
        return False
    return True       
        
def validate_bst(node, min_val, max_val):
    """
    This solution uses ranges of values to check that all nodes in left subtree are smaller
    than or equal to node.data, and all nodes in right subtree are greater than node. This is
    the ideal solution and works with duplicates also.
    """
    if not node:
        return True
    self_is_bst = (node.data >= min_val) and (node.data < max_val)
    left_is_bst = validate_bst(node.left, min_val, node.data)
    right_is_bst = validate_bst(node.right, node.data, max_val)
    if self_is_bst and left_is_bst and right_is_bst:
        return True
    return False

def validate_helper(root):
    return validate_bst(root, -sys.maxint, sys.maxint)

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(12)

print validate_helper(root)
print validate_in_order(root)

def easy_bst_check(node, in_order_list):
    """
    Not the most optimal but straight forward: do DFS and insert nodes into list.
    Then check if the list is sorted. This does NOT handle duplicates.
    """
    if not node:
        return
    easy_bst_check(node.left, in_order_list)
    in_order_list.append(node)
    easy_bst_check(node.right, in_order_list)

def easy_bst_helper(root):
    in_order_list = []
    easy_bst_check(root, in_order_list)
    print [i.data for i in in_order_list]
    return all(x.data < y.data for x, y in zip(in_order_list, in_order_list[1:]))

# print validate_in_order(root)
# print validate_bst(root)