from linked_list import Node, LinkedList
# 2.6 Palindrome
# ==============================================================================================
# Implement a function to check if a linked list is a palindrome
# ==============================================================================================
def palindrome(head):
	"""
	Use stack to insert all elements in list, then pop items out while traversing through list
	again
	"""
    stack = list()
    node = head
    while node:
        stack.append(node)
        node = node.next_node
    node = head
    print [i.data for i in stack]
    while node:
        other = stack.pop()
        if node.data != other.data:
            return False # not palindrome
        node = node.next_node
    return True

print palindrome(LinkedList([1,2,3,2,1]).head)
print palindrome(LinkedList([1,2,3,4,6]).head)

def reverse(node):
    head = None
    while node:
        new = Node(node.data)
        new.next_node = head
        head = new
        node = node.next_node
    return head
        
# my_list = LinkedList([1,2,3])
# node = reverse(my_list.head)
# while node:
#     print node.data
#     node = node.next_node
    
def palindrome_by_reversal(head):
    reversal = reverse(head)
    runner_1 = head
    runner_2 = reversal
    while runner_1:
        if runner_1.data != runner_2.data:
            return False # not a palindrome
        runner_1 = runner_1.next_node
        runner_2 = runner_2.next_node
    return True

print palindrome_by_reversal(LinkedList([1,2,3,2,1]).head) # TRUE
print palindrome_by_reversal(LinkedList([1,2,7,8,9]).head) # FALSE

