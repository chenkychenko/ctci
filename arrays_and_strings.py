################################################################################################
# CTCI 1: ARRAYS AND STRINGS
################################################################################################

# 1.1 Is Unique
# ==============================================================================================
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# ==============================================================================================

def is_unique_counts(s):
    """
    This solution runs in O(N) time using O(1) extra space
    """
    if len(s) > 128:
        return False
    char_list = [False] * 128
    print char_list
    for char in s:
        if char_list[ord(char)]:
            return False # we've seen this character before
        else:
            char_list[ord(char)] = True
    print char_list
    return True

print is_unique_counts("liourew")

def is_unique_bitvector(s):
    return False # in progress
    
def is_unique_set(string):
    """
    This solution runs in O(N) time using O(1) extra space (how many characters there are)
    """
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

# print is_unique_set("diana")

# BRUTE FORCE IMPLEMENTATION
def is_unique_brute(string):
    """
    This solution runs in O(N2) time and uses O(1) space
    """
    for i in range(len(string)):
        for k in range(i+1, len(string)):
            if string[i] == string[k]:
                return False
    return True

# print is_unique_brute("qweuijkhfs")

# 1.2 Check Permutation
# ==============================================================================================
# Given two strings, write a method to decide if one is a permutation of the other
# ==============================================================================================

def is_permutation_counts(a,b):
    """
    This solution uses an array to count frequencies of each character occurring
    Then goes through the second array decrementing
    Runtime is O(N) using O(1) extra space (array that is 128 chars)
    """
    if len(a) != len(b):
        return False

    letters = [0] * 128 # assumption this is ASCII
    for char in a:
        letters[ord(char)] += 1
    for char in b:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True

# not using any extra space at all:
def is_permutation_sort(a, b):
    """
    This solution runs in O(NlogN) time and uses O(1) space
    """
    return sorted(a) == sorted(b)

# print is_permutation_count("diana", "andia")
# print is_permutation_sort("diana", "andia")

# 1.3 URLify
# ==============================================================================================
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the 
# "true" length of the string.
# ==============================================================================================

def urlify(a, true_len):
    """
    This solution 'cheats' and creates a list of python characters it then joins together
    This solution is not technically done in place. 
    Runtime is O(N) to scan through char array, then to join list. Uses O(N) extra space
    """
    urlified = []
    for i in range(true_len):
        if a[i] == " ":
            urlified.append("%20")
        else:
            urlified.append(a[i])
    return ''.join(urlified)

print urlify("Mr John Smith    ", 13)

def urlify_inplace(a, true_len):
    a = list(a)
    k = true_len-1
    i = len(a)-1
    while i >= 0 and k >= 0:
        if a[k] != " ":
            a[i] = a[k]
            i -= 1
            k -= 1
        else:
            a[i] = "0"
            a[i-1] = "2"
            a[i-2] = "%"
            i -= 3
            k -= 1
    return ''.join(a)

print urlify_inplace("Mr John Smith    ", 13)

# 1.4 Palindrome Permutation
# ==============================================================================================
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome 
# is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
# of letters. The palindrome does not need to be limited to just dictionary words.
# ==============================================================================================
def palindrome_permutation(a):
    # might need to convert upper case to lower case - go through array once and convert
    letters = [0] * 128 # assume ASCII
    num_spaces = 0
    for char in a:
        if char != " ":
            letters[ord(char)] = not letters[ord(char)]
        else:
            num_spaces += 1
    count = 0
    for l in letters:
        if l:
            count += 1
    if count <= 1:
        return True
    return False # any other combination

print palindrome_permutation("are we not drawn onward to new era")
print palindrome_permutation("poop")
print palindrome_permutation("the city")

# 1.5 One Away
# ==============================================================================================
# There are three types of edits that can be performed on strings: insert a character, remove a
# character or replace a character. Given two strings, write a function to check if they are one
# edit (or zero edits) away.
# ==============================================================================================
def one_edit_away(a, b):
    """
    First, we check that the length does not differ by more than 1 - if it does, then we know that
    the two strings are more than 1 edit away. Otherwise, we break it down into two cases:
    insertion/deletion or replacement.
    
    Runtime is O(N) and space complexity is O(1) (if counting converting strings to lists then O(N))
    """
    a = list(a)
    b = list(b)
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) > len(b):
        return one_edit_insert(b,a)
    elif len(a) < len(b):
        return one_edit_insert(a,b)
    else:
        return one_edit_replace(a,b)

def one_edit_insert(a,b):
    """
    Iterate through both strings simultaneously and check when an extra character is enountered.
    Runtime is O(N) and O(1) space.
    """
    i = 0
    k = 0
    while i < len(a) and k < len(b):
        if a[i] != b[k]:
            if i != k:
                return False
            k += 1
        else:
            i += 1
            k += 1
    return True

def one_edit_replace(a,b):
    """
    Iterate through both strings simultaneously and note when the replacement has been found. From
    there just make sure there are no more replacements.
    Runtime is O(N) with O(1) space used.
    
    """
    replacement_found = False
    for i in range(len(a)): # length is the same
        if a[i] != b[i]:
            if replacement_found:
                return False
            replacement_found = True
    return True

print one_edit_away('pale', 'slepa') # two replacements, should be false
print one_edit_away('poop', 'polp')
print one_edit_away('diana', 'dianai')

# OPTIMIZED VERSION: do all cases in one method
def one_edit_merged(a, b):
    a = list(a)
    b = list(b)
    if abs(len(a) - len(b)) > 1:
        return False
    
    shorter = a if len(a) < len(b) else b
    longer = b if len(a) < len(b) else a
    print "shorter: {}, longer: {}".format(shorter, longer)
    found_difference = False
    i = 0
    k = 0
    while i < len(shorter) and k < len(longer):
        print i, k
        if shorter[i] != longer[k]:
            if found_difference:
                return False
            found_difference = True
            if len(shorter) == len(longer):
                i += 1
        else:
            i += 1
        k += 1
    return True

print one_edit_merged('pale', 'pales')
print one_edit_merged('pale', 'pal')
print one_edit_merged('pale', 'bake') # FALSE