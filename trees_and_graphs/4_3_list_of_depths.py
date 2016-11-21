# 4.3 List of Depths
# ==============================================================================================
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each
# depth (e.g., if you have a tree with depth D, you'll have D linked lists).
# ==============================================================================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque
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
            
def list_of_depths(root):
    depths = [[]]
    queue = deque([])
    queue.append((root, 0))
    while queue:
        cur_node, depth = queue.popleft()
        if len(depths) == depth:
            depths.append([])
        depths[depth].append(cur_node)
        if cur_node.left:
            queue.append((cur_node.left, depth+1))
        if cur_node.right:    
            queue.append((cur_node.right, depth+1))
    return depths

root = Node(1)
root.left = Node(5)
root.right = Node(3)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(2)
root.right.right = Node(7)

print_tree(root)

print "GETTING LIST OF DEPTHS!"
depth_list = list_of_depths(root)
for depth in depth_list:
    print [node.data for node in depth]