# 3.1 Three in One
# ==============================================================================================
# Describe how you could use a single array to implement three stacks
# ==============================================================================================
class MultiStack(object):
    def __init__(self, capacity, num_stacks):
        self.stacks = [0] * capacity * num_stacks
        self.capacity = capacity
        self.num_stacks = num_stacks
        self.sizes = [0] * num_stacks

    def pop(self, num_stack):
        if self.is_empty(num_stack):
            raise Exception("Stack is empty!")
        offset = num_stack * self.capacity + self.sizes[num_stack] - 1
        item = self.stacks[offset]
        self.stacks[offset] = 0 # reset
        self.sizes[num_stack] -= 1
        return item
                
    def push(self, num_stack, item): # num_stack is 0-based
        if self.is_full(num_stack):
            raise Exception("Stack is full!")
        self.sizes[num_stack] += 1 # increment size
        offset = num_stack * self.capacity + self.sizes[num_stack] - 1
        self.stacks[offset] = item
        
    def peek(self, num_stack):
        offset = num_stack * self.capacity + self.sizes[num_stack] - 1
        return self.stacks[offset]
        
    def is_empty(self, num_stack):
        return self.sizes[num_stack] == 0
        
    def is_full(self, num_stack):
        return self.sizes[num_stack] == self.capacity
    
mstack = MultiStack(5, 3)
mstack.push(1, 5)
print mstack.stacks
print mstack.sizes
mstack.pop(1)
print mstack.stacks