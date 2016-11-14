from linked_list import Node, LinkedList
# 2.2 Return Kth to Last
# ==============================================================================================
# Implement an algorithm to find the kth to last element of a singly linked list.
# ==============================================================================================
def kth_to_last(head, k):
    node = head
    runner = node
    for i in range(k):
        if not runner:
            raise Exception("List too short!")
        runner = runner.next_node
    while runner:
        node = node.next_node
        runner = runner.next_node
    return node

print kth_to_last(LinkedList([7,6,5,4,3,2,1]).head, 2).data
print kth_to_last(LinkedList([7,6,5,4,3,2,1]).head, 10).data

# class WrapperNode(object):
# 	index = 0
# 	node = None

def kth_to_last_rec(node, k):
    if not node:
        return 0
    index = kth_to_last_rec(node.next_node, k) + 1
    if index == k:
        print "Kth to last node is: {}".format(node.data)
    return index

kth_to_last_rec(LinkedList([7,6,5,4,3,2,1]).head, 5)

