# 8.4 Power Set
# ==============================================================================================
# Write a method to return all subsets of a set.
# ==============================================================================================
def get_subsets_helper(my_set):
    subsets = []
    get_subsets(my_set, 1, subsets)
    return subsets

def get_subsets(my_set, index):
    all_subsets = []
    if len(my_set) == index:
        all_subsets.append([]) # empty set
    else:
        all_subsets = get_subsets(my_set, index+1)
        item = my_set[index]
        more_subsets = []
        for subset in all_subsets:
            more_subsets.append(subset[:].append(item))
    all_subsets.append()
        
def get_subsets(my_set):
    result_sets = [[]]
    for item in my_set:
        item_sets = []
        for result_set in result_sets:
            item_set.append(result_set[:].append(item))
        result_sets.extend(item_sets)

def get_subsets(my_set):
    return get_subsets_helper(my_set)
    
def get_subsets_helper(my_set, result_sets=None):
    if not result_sets:
        result_sets = [[]]
    if not my_set:
        return result_sets
    item = my_set.leftpop()
    item_sets = []
    for result_set in result_sets:
        item_sets.append(result_set[:].append(item))
    result_sets.extend(item_sets)
    return get_subsets_helper(my_set, result_sets)