class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 4.12 Paths with Sum
# ==============================================================================================
# You are given a binary tree in which each node contains an integer value (which might be 
# positive or negative). Design an algorithm to count the number of pahts that sum to a given
# value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
# ==============================================================================================
def get_paths(node, val, sum_list):
    if not node:
        return
    paths_with_sum(node, 0, val, [], sum_list)
    paths_with_sum(node.left, 0, val, [], sum_list)
    paths_with_sum(node.right, 0, val, [], sum_list)

def paths_with_sum(node, cur_sum, val, cur_list, sum_list):
    if not node:
        return
    cur_list.append(node)
    cur_sum += node.data
    if cur_sum == val:
        sum_list.append(cur_list)
    paths_with_sum(node.left, cur_sum, val, cur_list[:], sum_list)
    paths_with_sum(node.right, cur_sum, val, cur_list[:], sum_list)
    
def paths_helper(root, val):
    sum_list = []
    get_paths(root, val, sum_list)
    return sum_list

root = Node(5)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(-1)
root.right.left = Node(-1)
root.right.right = Node(-5)

sums = paths_helper(root, 3)
for s in sums:
    print [i.data for i in s]