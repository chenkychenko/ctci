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
            
# 4.10 Check Subtree
# ==============================================================================================
# T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to
# determine if T2 is a subtree of T1. A tree T2 is a subtree of T1 if there exists a node n in
# T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n,
# the two trees would be identical.
# ==============================================================================================
def is_subtree(t1_node, t2_root):
    if not t1_node:
        return None
    if t1_node is t2_root: # found beginning of possible subtree
        print "FOUND NODE: {}".format(t1_node.data)
        res = check_subtree(t1_node, t2_root)
        if res:
            return t1_node
    return is_subtree(t1_node.left, t2_root) or is_subtree(t1_node.right, t2_root)

def check_subtree(node_1, node_2):
    if not node_1 and not node_2:
        return True
    if node_1 is not node_2:
        return False
    left_equal = check_subtree(node_1.left, node_2.left)
    right_equal = check_subtree(node_1.right, node_2.right)
    return left_equal and right_equal

root = Node(4)
root.left = Node(1)
root.right = Node(2)
root.right.right = Node(3)
root.right.left = Node(6)
root.right.left.left = Node(8)
root.right.left.right = Node(9)

t2 = root.right.left

print is_subtree(root, t2).data



    