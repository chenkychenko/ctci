# 4.4 Check Balanced
# ==============================================================================================
# Implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
# never differ by more than one.
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
            
def check_balanced(node):
    if not node:
        return (0, True) # height here is 0
    height_left, left_bal = check_balanced(node.left)
    height_right, right_bal = check_balanced(node.right)
    print "left height: {}, balanced? {}".format(height_left, left_bal)
    print "right height: {}, balanced? {}".format(height_right, right_bal)
    if not left_bal or not right_bal:
        return (max(height_left, height_right), False)
    if abs(height_left - height_right) > 1:
        return (max(height_left, height_right), False)
    return (max(height_left, height_right) + 1, True)

def get_height(node):
    if not node:
        return -1
    return abs(get_height(node.left), get_height(node.right)) + 1

def is_balanced(node):
    if not node:
        return False
    height_diff = abs(get_height(node.left) - get_height(node.right))
    if height_diff > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)
    
root = Node(1)
root.left = Node(5)
root.right = Node(3)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(2)
root.right.right = Node(7)


print check_balanced(root)
            
