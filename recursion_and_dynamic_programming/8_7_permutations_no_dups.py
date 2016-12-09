# 8.7 Permutations without Dups
# ==============================================================================================
# Write a method to compute all permutations for a string of unique chatacters.
# ==============================================================================================
def permute(word):
    """
    Creates permutations by starting with empty string, then inserting char into all previous
    results, in every index of previous permutation.
    :param word: string, word to permute
    :return: list of permutations (as list of chars)
    """
    results = []
    if not word: # no more characters left
        results.append([''])
        return results # base case
    char = word.pop()
    words = permute(word)
    for perm in words:
        new_perms = insert_in_every_location(perm, char)
        results.extend(new_perms)
    return results

def insert_in_every_location(perm, char):
    result = []
    for i in range(len(perm)):
        new_perm = perm[:]
        new_perm.insert(i, char)
        result.append(new_perm)
    return result

res = permute(list('abcd'))
print [''.join(i) for i in res]

def get_perms(prefix, remainder, result):
    """
    This method computes permutations by "trying" each character as a first character in the
    permutation.
    :param prefix: the set string prefix for the permutation that is being built
    :param remainder: remaining chars to use in permutation generation
    :param result: list of strings which are permutations, this gets filled as we go
    :return: void method, just fills up the list that gets passed in (we pass in empty list at
    the beginning.
    """
    if not remainder:
        result.append(prefix) # we have a permutation
    for i in range(len(remainder)):
        new_rem = remainder[:]
        char = new_rem.pop(i)
        get_perms(prefix + char, new_rem, result)

def get_perms_helper(word):
    result = []
    get_perms('', list(word), result)
    return result

print get_perms_helper('abcd')