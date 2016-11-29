# 4.9 BST Sequences
# ==============================================================================================
# A binary search tree was created by traversing through an array from left to right and
# inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# ==============================================================================================
def all_sequences(node):
    sequences = []
    if not node:
        sequences.append([])
        return sequences

    prefix = []
    prefix.append(node.data)
    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)

    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            sequences.extend(weaved)
    return sequences

def weave_lists(first, second, results, prefix):
    # remove from first list, put in prefix
    if not first or not second: # time to print!
        seq = first.extend(second)
        results.append(seq)
        return
    
    # start with first and move into prefix
    val = first.pop(0) # remove from front
    prefix.append(val)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, val)
    
    # now do the second pair weaving
    val = second.pop(0)
    prefix.append(val)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, val)