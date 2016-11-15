from linked_list import Node, LinkedList
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

# ==============================================================================================
# FOLLOWUP: Suppose the digits are stored in forward order. Repeat the above problem.
# ==============================================================================================
def sum_lists_helper(l1, l2):
    l1_length = get_length(l1)
    l2_length = get_length(l2)
    if l1_length > l2_length:
        pad_zeroes(l2, l1_length - l2_length)
    else:
        pad_zeroes(l1, l2_length - l1_length)
    node, carry = sum_lists_forward(l1, l2)
    if carry == 0:
        return node
    else:
        return insert_before(node, carry)

def pad_zeroes(node, count):
    while node.next_node:
        node = node.next_node
    for i in range(count):
        new_node = Node(0)
        node.next_node = new_node
        node = new_node
        
def sum_lists_forward(l1, l2):
    if not l1 and not l2:
        return (None, 0)
    node, carry = sum_lists_forward(l1.next_node, l2.next_node)
    val = carry + l1.data + l2.data
    full_result = insert_before(node, val % 10)
    return (full_result, val / 10)

def get_length(node):
    count = 0
    while node:
        count += 1
        node = node.next_node
    return count
    
def insert_before(head, data):
    node = Node(data)
    if head:
        node.next_node = head
    return node

l1 = LinkedList([9,7,8])
l2 = LinkedList([6,8,5])
n = sum_lists_helper(l1.head,l2.head)
while n:
    print n.data
    n = n.next_node