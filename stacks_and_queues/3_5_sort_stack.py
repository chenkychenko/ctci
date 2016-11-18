from stack import StackNode, Stack
# 3.5 Sort Stack
# ==============================================================================================
# Write a program to sort a stack usch that the smallest items are on the top. You can use an
# additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
# ==============================================================================================
def sort_stack(stack):
    temp = Stack()
    while not stack.is_empty(): 
        element = stack.pop()
        while not temp.is_empty() and element > temp.peek():
            stack.push(temp.pop()) # keep popping and pushing
        temp.push(element)
    return temp

stack = Stack()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(9)
stack.print_stack()

sorted_stack = sort_stack(stack)
print "SORTED STACK:"
sorted_stack.print_stack()