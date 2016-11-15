from linked_list import LinkedList, Node
# 2.4 Partition
# ==============================================================================================
# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is container within the list, the values of 
# x only need to be after the elements less than x. The partition element x can appear anywhere
# in the "right partition"; it does not need to appear between the left and right partitions.
# ==============================================================================================
def partition(head, k):
    node = head
    tail = head
    while node:
        next_node = node.next_node
        if node.data < k: # append to left of head
            node.next_node = head
            head = node
        else:
            tail.next_node = node
            tail = node
        node = next_node
    tail.next_node = None
    return head

node = partition(LinkedList([4,7,3,6,5,2,3]).head, 4)
while node:
    print node.data
    node = node.next_node