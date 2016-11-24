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
    """
    Straight forward recursive approach - at each node, check if node_1 is in left subtree and if
    node_2 is in the right subtree. If both in the same subtree, move in that direction. If node_1
    and nod_2 in different subtrees, you have found the first common ancestor, so we return it. 
    """
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

def common_ancestor(root, node_1, node_2):
    """
    Optimied approach where we don't keep researching each subtree for node_1 and node_2
    Before using this method we need to make sure that both node_1 and node_2 exist in the
    tree.
    """
    if not root:
        return None
    if root is node_1 or root is node_2:
        return root
    
    left_node = common_ancestor(root.left, node_1, node_2)
    if left_node and left_node is not node_1 and left_node is not node_2:
        return left_node # found common ancestor
    
    right_node = common_ancestor(root.right, node_1, node_2)
    if right_node and right_node is not node_1 and right_node is not node_2:
        return right_node # found common ancestor
    if left_node and right_node:
        return root # this is common ancestor since node_1 and node_2 in diff subtrees
    if root is left_node or root is right_node:
        return root
    res = left_node if left_node else right_node
    return res
