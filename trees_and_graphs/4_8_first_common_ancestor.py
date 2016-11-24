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

# 4.8 First Common Ancestor
# ==============================================================================================
# Design an algorithm and write code to find the first common ancestor of two nodes in a binary
# tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a 
# binary search tree.
# ==============================================================================================
def first_common_ancestor(root, node_1, node_2):
    node1_in_left = find_node(root.left, node_1)
    node2_in_right = find_node(root.right, node_2)
    if ((node1_in_left and node2_in_right) or 
        (not node1_in_left and not node2_in_right)): # found our common ancestor!
            return root
    if node1_in_left:
         return first_common_ancestor(root.left, node_1, node_2)
    if node2_in_right:
         return first_common_ancestor(root.right, node_1, node_2)
    
def find_node(node, target):
    if not node:
        return False
    is_in_left = find_node(node.left, target)
    is_in_right = find_node(node.right, target)
    if is_in_left or is_in_right or (node is target):
        return True
    return False

node_1 = Node(16)
node_2 = Node(32)
root = Node(1)
root.left = Node(2)
root.right = Node(6)
root.left.left = node_2
root.left.right = node_1

node = first_common_ancestor(root, node_1, node_2)   
if node:
    print node.data
    