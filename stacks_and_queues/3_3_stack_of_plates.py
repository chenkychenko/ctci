# 3.3 Stack of Plates
# ==============================================================================================
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
# in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack. (that is,
# pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
# ==============================================================================================
class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class Stack(object):
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.size = 0
        
    def pop(self):
        if not self.top:
            raise Exception("Stack is empty!")
        item = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return item
        
    def push(self, item):
        if self.is_full():
            raise Exception("Cannot push, stack is at capacity!")
        node = StackNode(item)
        node.next_node = self.top
        self.top = node
        self.size += 1
    
    def peek(self):
        if not self.top:
            raise Exception("Stack is empty!")
        return self.top.data
    
    def is_empty(self):
        return self.top == None
    
    def is_full(self):
        return self.size == self.capacity
    
    def print_stack(self):
        print "PRINTING STACK:"
        node = self.top
        while node:
            print node.data
            node = node.next_node
            
class SetOfStacks(object):
    def __init__(self, capacity):
        self.stacks = [Stack(capacity)]
        self.top = None
        self.capacity = capacity
    
    def push(self, item):
        stack_to_use = self.get_last_stack()
        if not stack_to_use.is_full():
            stack_to_use.push(item)
        else:
            new_stack = Stack(self.capacity)
            self.stacks.append(new_stack)
            new_stack.push(item)
    
    def pop(self):
        stack_to_use = self.get_last_stack()
        if not stack_to_use:
            raise Exception("No stacks, everything empty!")
        item = stack_to_use.pop()
        if stack_to_use.is_empty():
            self.stacks.pop()
        return item
            
    def get_last_stack(self):
        return self.stacks[-1]
    

my_stack = SetOfStacks(2)
my_stack.push(2)
my_stack.push(3)
my_stack.push(6)
for stack in my_stack.stacks:
    stack.print_stack()    
my_stack.pop()
for stack in my_stack.stacks:
    stack.print_stack()