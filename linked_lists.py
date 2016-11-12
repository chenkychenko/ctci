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
def remove_dupes(node):
    dupes = set()
    prev = None
    while node:
        if node.data in dupes:
            prev.next_node = node.next_node
        else:
            dupes.add(node.data)
            prev = node
        node = node.next_node

ml = LinkedList([1,1,1,2,2,3,6,5,4,5,2,3,8,7,6,5,4,3,9])
remove_dupes(ml.head)
node = ml.head
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

# 2.4 Partition
# ==============================================================================================
# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is container within the list, the values of 
# x only need to be after the elements less than x. The partition element x can appear anywhere
# in the "right partition"; it does not need to appear between the left and right partitions.
# ==============================================================================================
def partition(head, k):
    if not head or not head.next_node:
        return None # list is empty or only one element
    
    node = head
    last = None
    length = 0
    while node:
        length += 1
        if not node.next_node:
            last = node
        node = node.next_node
    
    node = head
    prev = None
    count = 0
    while count < length:
        count += 1
        if node.data < k:
            prev = node
            node = node.next_node
        else: # need to move node to the end
            next_node = node.next_node
            if not prev:
                head = next_node
            else:
                prev.next_node = next_node        
            last.next_node = node
            last = node
            last.next_node = None    
            node = next_node
    return head

my_list = LinkedList([5,4,8,2,3,1,7])
node = partition(my_list.head, 3)
while node:
    print node.data
    node = node.next_node

def partition(node, k):
    head = node
    tail = node
    
    while node:
        next_node = node.next_node
        if node.data < k:
            node.next_node = head
            head = node
        else:
            tail.next_node = node
            tail = node
        node = next_node
    tail.next_node = None
    return head

# 2.4 Sum Lists
# ==============================================================================================
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1s digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# ==============================================================================================
def sum_lists(l1, l2, carry):
    if not l1 and not l2 and carry == 0:
        return None

    result = Node(None)
    value = carry
    if l1:
        value += l1.data
    if l2:
        value += l2.data

    result.data = value % 10 # get second digit
    if l1 and l2:
        l1 = l1.next_node if l1 else None
        l2 = l2.next_node if l2 else None
        value = 1 if value >= 10 else 0
        more = sum_lists(l1, l2, value)
        result.next_node = more
    return result

a = LinkedList([5,4,8])
b = LinkedList([1,2,4])
res = sum_lists(a.head, b.head, 0)

while res:
    print res.data
    res = res.next_node
