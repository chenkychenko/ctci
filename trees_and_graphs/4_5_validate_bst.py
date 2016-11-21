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

def check_bst(node, min_val, max_val):
    """
    In order traversal will make sure that binary tree is BST if each element is greater than
    previous.
    """
    if not node:
        return True
    new_val = node.data
    left_in_range = check_bst(node.left, min_val, new_val)
    right_in_range = check_bst(node.right, new_val, max_val)
    self_is_bst = True
    if node.left:
        self_is_bst = self_is_bst and (node.left.data <= new_val)
    if node.right:
        self_is_bst = self_is_bst and (node.right.data > new_val)
    return left_in_range and right_in_range and self_is_bst
    
def bst_helper(root):
    return check_bst(root, -sys.maxint, sys.maxint)

def easy_bst_check(node, in_order_list):
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
               
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(12)

print easy_bst_helper(root)
print bst_helper(root)