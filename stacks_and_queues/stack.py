class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class Stack(object):
    def __init__(self):
        self.top = None
        
    def pop(self):
        if not self.top:
            raise Exception("Stack is empty!")
        item = self.top.data
        self.top = self.top.next_node
        return item
        
    def push(self, item):
        node = StackNode(item)
        node.next_node = self.top
        self.top = node
    
    def peek(self):
        if not self.top:
            raise Exception("Stack is empty!")
        return self.top.data
    
    def is_empty(self):
        return self.top == None
    
    def print_stack(self):
        node = self.top
        while node:
            print node.data
            node = node.next_node