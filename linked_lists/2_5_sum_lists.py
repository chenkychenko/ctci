# 2.4 Sum Lists
# ==============================================================================================
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1s digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# ==============================================================================================
def sum_lists(l1, l2, carry):
    if not l1 and not l2 and carry == 0:
        return None
    result = carry
    if l1:
        result += l1.data
    if l2:
        result += l2.data
    
    node = Node(result % 10)
    if l1 or l2:
        l1 = l1.next_node if l1 else None
        l2 = l2.next_node if l2 else None
        node.next_node = sum_lists(l1, l2, result / 10)
    return node

l1 = LinkedList([7,1,6,7,8])
l2 = LinkedList([5,9,2])
n = sum_lists(l1.head,l2.head,0)
while n:
    print n.data
    n = n.next_node