# 4.2 Minimal Tree
# ==============================================================================================
# Given a sorted (increasing order) array with unique integer elements, write an algorithm to
# create a binary search tree with minimal height
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

def minimal_tree(start, end, array):
    if end < start: # base case
        return None
    print "start: {}, end: {}".format(start, end)
    midpoint = (start + end)/2
    node = Node(array[midpoint])
    node.left = minimal_tree(start, midpoint-1, array)
    node.right = minimal_tree(midpoint+1, end, array)
    return node

def create_binary_tree(array):
    return minimal_tree(0, len(array)-1, array)

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
root = create_binary_tree(array)
print_tree(root)