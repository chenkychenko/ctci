# 4.7 Build Order
# ==============================================================================================
# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's
# dependencies must be build before the project is. Find a build order that will allow the
# projects to be built. If there is no valid build order, return an error.
# ==============================================================================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.adjacency_list = []

class Graph(object):
    def __init__(self):
        self.nodes = []
        
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

def build_graph(projects, dependencies):
    # first create nodes for each project
    graph = Graph()
    for p in projects:
        graph.nodes.append(Node(p))
    # now we iterate through dependencies, making edhes between nodes
    for first, second in dependencies:
        first_node = get_node(first, graph)
        second_node = get_node(second, graph)
        second_node.adjacency_list.append(first_node)
    return graph
        
def get_node(val, graph):
    nodes = graph.nodes
    for i in range(len(nodes)):
        if nodes[i].data == val:
            return nodes[i]
    return None

def build_order(node, parent):
    if not node:
        return
    # parent.
    for n in node.adjacency_list:
        build_order(n, node)
    
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
graph = build_graph(projects, dependencies)
for i in graph.nodes:
    print i.data, [k.data for k in i.adjacency_list]
    

        
        
