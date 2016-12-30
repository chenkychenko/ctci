# 10.2 Group Anagrams
# ==============================================================================================
# Write a method to sort an array of strings so that all the anagrams are next to each other.
# ==============================================================================================
def group_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_sorted = ''.join(sorted(s))
        if s_sorted not in anagrams:
            anagrams[s_sorted] = [s]
        else:
            anagrams.get(s_sorted).append(s)
    sorted_list = []
    for key, value in anagrams.iteritems():
        sorted_list.extend(value)
    return sorted_list

strings = ["acb", "tar", "cba", "cab", "rat"]
print group_anagrams(strings)