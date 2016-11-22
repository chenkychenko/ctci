class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

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

# 4.6 Successor
# ==============================================================================================
# Write an algorithm to find the "next" node (ie, in-order successor) of a given node in a binary
# search tree. You may assume that each node has a link to its parent.
# ==============================================================================================
def get_successor(node):
    if not node:
        return None
    if node.right:
        return get_leftmost_node(node.right)
    # now, there is no right subtree, next is in parent if child is left
    while node.parent and node.parent.left is not node: # while node is not left child, recurse up
        node = node.parent
    return node.parent

def get_leftmost_node(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

root = Node(5)
root.left = Node(3)
root.left.parent = root
root.right = Node(8)
root.right.parent = root
root.left.left = Node(1)
root.left.left.parent = root.left
root.left.right = Node(4)
root.left.right.parent = root.left

next_node = get_successor(root.left.right)
if next_node:
    print next_node.data
else:
    print "NO SUCESSOR"