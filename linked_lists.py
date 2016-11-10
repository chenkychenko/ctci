################################################################################################
# CTCI 2: LINKED LISTS
################################################################################################

class Node(object):
    next_node = None
    data = None

    def __init__(self, data):
        self.data = data
    
class LinkedList(object):
    head = None # pointer to first node
    
    def __init__(self, real_list):
        if real_list:
            self.head = Node(real_list[0])
            node = self.head
            for i in range(1,len(real_list)):
                node.next_node = Node(real_list[i])
                node = node.next_node


# 2.1 Remove Dupes
# ==============================================================================================
# Write code to remove duplicates from an unsorted linked list.
# Followup: how would you solve this problem if a temporary bugger is not allowed?
# ==============================================================================================
def remove_dupes(head):
    if not head:
        raise Exception("Head pointer is null")
    dupe_counts = {}
    cur_node = head
    while cur_node:
        if cur_node.data not in dupe_counts:
            dupe_counts[cur_node.data] = 1
        else:
            dupe_counts[cur_node.data] += 1
        cur_node = cur_node.next_node
    cur_node = head
    while cur_node.next_node:
        if dupe_counts[cur_node.next_node.data] > 1: # duplicate
            dupe_counts[cur_node.next_node.data] -= 1
            cur_node.next_node = cur_node.next_node.next_node
        cur_node = cur_node.next_node
    return head

my_list = [1,2,3,4,4,5,6,3,3]
my_list = LinkedList(my_list)

node = remove_dupes(my_list.head)

while node:
    print node.data
    node = node.next_node
    
def remove_dupes_no_buffer(head):
    if not head:
        raise Exception("Head pointer is null")
    first = head
    while first:
        cur_node = first
        while cur_node.next_node:
            if cur_node.next_node.data == first.data:
                cur_node.next_node = cur_node.next_node.next_node
            cur_node = cur_node.next_node
        first = first.next_node
    return head

node = remove_dupes_no_buffer(my_list.head)
while node:
    print node.data
    node = node.next_node   

# 2.2 Return Kth to Last
# ==============================================================================================
# Implement an algorithm to find the kth to last element of a singly linked list.
# ==============================================================================================
def kth_to_last(head, k):
    if not head:
        raise Exception("List is empty")
    cur_node = head
    count = 0
    while cur_node and count < k:
        count += 1
        cur_node = cur_node.next_node
    if count < k:
        return None # list is too short
    runner = cur_node
    # print runner.data
    cur_node = head
    while runner:
        runner = runner.next_node
        cur_node = cur_node.next_node
    return cur_node.data

my_list = [1,2,3,4,5,6,7,8,9]
my_list = LinkedList(my_list)
print kth_to_last(my_list.head, 4)  

# recursive approach; this one requires printing
def print_kth_to_last(node, k):
    if not node:
        return 0
    index = print_kth_to_last(node.next_node, k) + 1
    if index == k:
        print "kth to last node is: {}".format(node.data)
    return index

# 2.3 Delete Middle Node
# ==============================================================================================
# Implement an algorithm to delete a node in the middle (ie, any node but the first and last
# node, not necessarily the exact middle) of a singly linked list, given only access to that node
# ==============================================================================================
def delete_middle(node):
    if not node.next_node:
        raise Exception("Trying to delete last node")
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node

my_list = [1,2,3,4,5,6,7,8,9]
my_list = LinkedList(my_list)

n = my_list.head.next_node.next_node # delete 3!
delete_middle(n)
node = my_list.head
while node:
    print node.data
    node = node.next_node
        