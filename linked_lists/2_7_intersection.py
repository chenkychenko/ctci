from linked_list import Node, LinkedList
# 2.7 Intersection
# ==============================================================================================
# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting 
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the 
# second linked list, then they are intersecting.
# ==============================================================================================
def intersection(l1, l2):
    length1 = get_length(l1)
    length2 = get_length(l2)
    runner1 = l1
    runner2 = l2
    if length1 > length2:
        for i in range(length1-length2):
            runner1 = runner1.next_node
    elif length2 > length1:
        for i in range(length2-length1):
            runner2 = runner2.next_node
    while runner1:
        if runner1 is runner2: # found intersection
            return runner1
        runner1 = runner1.next_node
        runner2 = runner2.next_node
    return None
    
def get_length(node):
    count = 0
    while node:
        count += 1
        node = node.next_node
    return count