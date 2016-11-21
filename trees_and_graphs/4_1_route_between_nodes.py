# 4.1 Route Between Nodes
# ==============================================================================================
# Given a directed graph, design an algorithm to find out whether there is a route between two 
# nodes.
# ==============================================================================================
from collections import deque

class Node(object):
    def __init__(self, data):
        self.data = data
        self.adjacency_list = []
        self.visited = False
        
class Graph(object):  
    def __init__(self):
        self.nodes = []

def find_route(node_1, node_2):
    """
    Use BFS from node_1 first to see if we can get to node_2. If we cannot, do BFS from node_2
    (since this is a directed graph)
    """
    if not node_1 or not node_2:
        raise Exception("One or both nodes is null!")
    if route_exists(node_1, node_2):
        return True
    else:
        return route_exists(node_2, node_1)

def route_exists(node, target):
    nodes_queue = deque([])
    nodes_queue.append(node)
    while nodes_queue: # means it's not empty
        cur = nodes_queue.popleft() # dequeue item
        print "now visitng node {}".format(cur.data)
        if cur is target:
            return True # found!
        cur.visited = True
        print "adjacency list of node {} is: {}".format(
                cur.data, [i.data for i in cur.adjacency_list])
        for n in cur.adjacency_list:
            print "node {} visited? {}".format(n.data, n.visited)
            if not n.visited:
                nodes_queue.append(n)
    return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.adjacency_list = [n2]
n2.adjacency_list = [n3]
n3.adjacency_list = [n4]
n4.adjacency_list = [n2]

print route_exists(n1, n2) # TRUE
print find_route(n1, n2) #  TRUE
print route_exists(n4, n1) # FALSE