from linked_list import Node, LinkedList
# 2.8 Loop Detection
# ==============================================================================================
# Given a circular linked list, implement an algorithm that returns the node at the beginning of
# the loop. DEFINITION: Circular linked list: a (corrupt) linked list in which a node's next
# pointer points to an earlier node, so as to make a loop in the linked list.
# ==============================================================================================
def loop_detection(node):
    """
    Using set to keep track of memory locations of each node. As soon as we see a memory location
    we have seen before, that is our loop node
    """
    seen = set()
    while node:
        if id(node) in seen:
            return node
        seen.add(id(node))
        node = node.next_node
    return None

def loop_detection_runners(node):
	"""
	Use two pointers, slow (1x) and fast (2x) to see whether they meet at the same node - if they
	meet that means we have a loop.
	"""
    # first iterate with two pointers, slow and fast
    slow = node
    fast = node

    # meeting point of slow and fast will be at (loop size - k) where k is length of list before loop
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow is fast:
            break
    if not fast and not fast.next_node: # no loop here
        return None
    
    slow = head # return slow back to the head
    while slow is not fast:
        slow = slow.next_node
        fast = fast.next_node
    return fast # return either fast or slow here since they are the same node