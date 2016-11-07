################################################################################################
# CTCI 1: ARRAYS AND STRINGS
################################################################################################

# 1.1 Is Unique
# ==============================================================================================
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# ==============================================================================================

def is_unique(s):
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

print is_unique("liourew")

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

def is_unique_brute(string):
    """
    This solution runs in O(N2) time and uses O(1) space
    """
    for i in range(len(string)):
        for k in range(i+1, len(string)):
            if string[i] == string[k]:
                return False
    return True

# print is_unique_brute("dialk")

# 1.2 Check Permutation
# ==============================================================================================
# Given two strings, write a method to decide if one is a permutation of the other
# ==============================================================================================

def is_permutation(a, b):
    """
    This solution runs in O(N) time and uses O(N) extra space
    """
    chars_in_a = {}
    chars_in_b = {}
    for char in a:
        if char in chars_in_a:
            chars_in_a[char] += 1
        else:
            chars_in_a[char] = 1
    for char in b:
        if char in chars_in_b:
            chars_in_b[char] += 1
        else:
            chars_in_b[char] = 1
    return chars_in_a == chars_in_b

# print is_permutation("diana", "andia")

# not using extra space:
def is_permutation_2(a, b):
    """
    This solution runs in O(NlogN) time and uses O(1) space
    """
    return sorted(a) == sorted(b)

# 1.3 URLify
# ==============================================================================================
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the 
# "true" length of the string.
# ==============================================================================================

def urlify(a, true_len):
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
# def palindrome_permutation(a):
    


# SORTING ALGOS
# bubble sort
# def bubble_sort(num_list):
#     for i in range(len(num_list)-1,0,-1):
#         for j in range(i):
#             if num_list[j] > num_list[j+1]:
#                 temp = num_list[j]
#                 num_list[j] = num_list[j+1]
#                 num_list[j+1] = temp
#     print num_list

# # selection sort
# def selection_sort(num_list):
#     for i in range(len(num_list)):
#         min_index = i # set the min first
#         for j in range(i+1, len(num_list)):
#             if num_list[j] < num_list[min_index]:
#                 min_index = j
#         temp = num_list[i]
#         num_list[i] = num_list[min_index]
#         num_list[min_index] = temp
#     print num_list

    
# # insertion sort
# def insertion_sort(num_list):
#     for i in range(1,len(num_list)):
#         temp = num_list[i]
#         k = i-1
#         while k >= 0 and temp < num_list[k]:
#             num_list[k+1] = num_list[k]
#             k -= 1
#         num_list[k+1] = temp
#     print num_list

# for i in range(10):
#     print i
 
# b = [6,9,2,1,5,4,8,0]
# print "NOW RUNNING BUBBLE SORT FOR LIST {}".format(b)
# bubble_sort(b)
# print "NOW RUNNING SELECTION SORT FOR LIST {}".format(b)
# selection_sort(b)
# print "NOW RUNNING INSERTION SORT FOR LIST {}".format(b)
# insertion_sort(b)
