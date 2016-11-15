from linked_list import LinkedList, Node
# 2.3 Delete Middle Node
# ==============================================================================================
# Implement an algorithm to delete a node in the middle (ie, any node but the first and last
# node, not necessarily the exact middle) of a singly linked list, given only access to that node
# ==============================================================================================
def delete_middle(node):
	if not node.next_node:
		raise Exception("Trying to delete last node!")
	node.data = node.next_node.data
	node.next_node = node.next_node.next_node

my_list = LinkedList([1,2,3,4,5,6,7,8,9])
n = my_list.head.next_node.next_node # delete 3!
delete_middle(n)
node = my_list.head

while node:
	print node.data
	node = node.next_node