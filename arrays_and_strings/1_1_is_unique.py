# 1.1 Is Unique
# ==============================================================================================
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# ==============================================================================================
def is_unique(s):
    char_counts = set()
    for char in s:
        if char in char_counts:
            return False
        char_counts.add(char)
    return True

print is_unique("diana")

def is_unique_brute(string):
    """
    This solution runs in O(N2) time and uses O(1) space
    """
    for i in range(len(string)):
        for k in range(i+1, len(string)):
            if string[i] == string[k]:
                return False
    return True

print is_unique_brute("qweuijkhfs")