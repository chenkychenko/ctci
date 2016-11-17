# 3.2 Stack Min
# ==============================================================================================
# How would you design a stack which, in addition to push and pop has a function min which
# returns the minimum element? Push, pop, and min should all operate in O(1) time.
# ==============================================================================================
class StackNode(object):
    def __init__(self, data, min_val):
        self.data = data
        self.min_val = min_val
        self.next_node = None
        
class StackWithMin(object):
    
    def __init__(self, top=None):
        if top:
            self.top = StackNode(top, top)
        else:
            self.top = None
    
    def push(self, item):
        if not self.top: # empty stack
            self.top = StackNode(item, item)
        else:
            if item < self.top.min_val:
                new_node = StackNode(item, item)
            else:
                new_node = StackNode(item, self.top.min_val)
            new_node.next_node = self.top
            self.top = new_node
    
    def pop(self):
        if not self.top: # empty stack
            raise Exception("Empty stack! Cannot pop")
        item = self.top.data
        self.top = self.top.next_node
        return item

    def get_min(self):
        if not self.top: # empty stack
            return Exception("Empty stack!")
        return self.top.min_val

stack = StackWithMin()
stack.push(6)
stack.push(4)
stack.push(2)
stack.push(8)
node = stack.top
while node:
    print "Data: {}, min: {}".format(node.data, node.min_val)
    node = node.next_node
print stack.get_min()