from linked_list import Node, LinkedList
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
    cur = head
    while cur:
        prev = cur
        runner = cur.next_node
        while runner:
            if runner.data == cur.data:
                prev.next_node = runner.next_node
            else:
                prev = runner
            runner = runner.next_node
        cur = cur.next_node
    return head

my_list = LinkedList([1,2,2,3,3,4,5,5,2,2])
res = remove_dupes_no_buffer(my_list.head)
node = res
while node:
    print node.data
    node = node.next_node 