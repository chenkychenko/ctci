class Node(object):
    next_node = None
    data = None

    def __init__(self, data):
        self.data = data
    
class LinkedList(object):
    head = None # pointer to first node
    
    def __init__(self, real_list):
        if real_list:
            self.head = Node(real_list[0])
            node = self.head
            for i in range(1,len(real_list)):
                node.next_node = Node(real_list[i])
                node = node.next_node