# 8.4 Power Set
# ==============================================================================================
# Write a method to return all subsets of a set.
# ==============================================================================================
def get_sets(my_set):
    """
    Generate all the sets by starting with the empty set, then inserting each character into the
    (n-1) generated sets.
    :param my_set: list of items - this is the set
    :return: list of lists containing all the subsets
    """
    if not my_set: # empty set, base case
        return [[]]
    next = my_set.pop()
    new_sets = []
    cur_set_list = get_sets(my_set)
    for cur_set in cur_set_list:
        new = cur_set[:]
        new.append(next)
        new_sets.append(new)
    cur_set_list.extend(new_sets)
    return cur_set_list

def calculate_sets(my_set):
    return get_sets(my_set)

res = calculate_sets([1,2,3,4])
print res