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
    """
    Most optimal solution: calculate height as we go, and as soon as we encounter
    imbalance, return False up the stack.
    """
    if not node:
        return (0, True) # balanced and height is 0
    left_height, left_balanced = check_balanced(node.left)
    right_height, right_balanced = check_balanced(node.right)
    height_diff = abs(left_height - right_height)
    new_height = max(left_height, right_height) + 1 # including node
    if left_balanced and right_balanced and height_diff <= 1:
        return (new_height, True)
    return (new_height, False)

def check_balanced_helper(root):
    _, balanced = check_balanced(root)
    return balanced

def get_height(node):
    """
    Extra recursive function just to find the height
    """
    if not node:
        return -1
    return max(get_height(node.left), get_height(node.right)) + 1

def is_balanced(node):
    """
    Less optimal solution where you have another recursive call to get the
    height of all the subtrees
    """
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


print check_balanced_helper(root)
            
