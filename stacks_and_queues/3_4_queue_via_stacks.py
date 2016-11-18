# 3.4 Queue via Stacks
# ==============================================================================================
# Implement a MyQueue class which implements a queue using two stacks
# ==============================================================================================
from stack import StackNode, Stack

class MyQueue(object):
    
    def __init__(self):
        self.stack_newest_top = Stack()
        self.stack_oldest_top = Stack()
        
    def remove(self):
        self.shift_stacks()
        return self.stack_oldest_top.pop()

    def add(self, item):
        self.stack_newest_top.push(item)
        
    def peek(self):
        self.shift_stacks()
        return self.stack_oldest_top.peek()
    
    def shift_stacks(self):
        if self.stack_oldest_top.is_empty():
            while not self.stack_newest_top.is_empty():
                self.stack_oldest_top.push(self.stack_newest_top.pop())
            
    def is_empty(self):
        return self.stack_newest_top.is_empty() and self.stack_oldest_top.is_empty()
        
queue = MyQueue()
queue.add(2)
queue.add(4)
queue.add(5)
queue.add(9)
print queue.remove()
print queue.remove()
print queue.remove()
queue.add(6)
print queue.remove()
print queue.remove()