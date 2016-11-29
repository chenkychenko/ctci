# 4.11 Random Node
# ==============================================================================================
# You are implementing a binary tree class from scratch which, in addition to insert, find, and
# delete, has a method get_random_node() which returns a random node from the tree. All nodes 
# should be equally likely to be chosen. Design and implement an algorithm for get_random_node()
# and explain how you would implement the rest of the methods.
# ==============================================================================================
from random import randint
def get_random_node(root):
    r = randint(0, 8)
    return dfs_count(root, r)
    
def dfs_count(node, num, stop):
    if not node:
        return None
    print "node is {}, num is {}".format(node.data, num)
    if num == stop:
        return node
    left = dfs_count(node.left, num+1, stop)
    right = dfs_count(node.right, num+2, stop)
    if left:
        return left
    if right:
        return right

# def get_nth_node(node):
#     if not node:
#         return 0
#     return 1 + get_nth_node(node.left) + get_nth_node(node.right)

count = 0
def get_nth_node(node, rand):
    if not node:
        return None
    global count
    count += 1
    print "node is {}, count is {}".format(node.data, count)
    if count == rand:
        print "RETURNING"
        return node
    left = get_nth_node(node.left, rand)
    right = get_nth_node(node.right, rand)
    if left:
        return left
    if right:
        return right
    # return (0, None)
    

node = get_nth_node(root, 4)
print node.data