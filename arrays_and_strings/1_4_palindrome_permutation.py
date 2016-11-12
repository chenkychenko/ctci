# 1.4 Palindrome Permutation
# ==============================================================================================
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome 
# is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
# of letters. The palindrome does not need to be limited to just dictionary words.
# ==============================================================================================
def palindrome_permutation(s1):
	char_counts = [False] * 128 # assume ASCII
	for char in s1:
		if char != " ":
			char_counts[ord(char)] = not char_counts[ord(char)]
	found_true = False
	for char in char_counts:
		if char:
			if found_true:
				return False
			found_true = True
	return True

print palindrome_permutation("tact coa")
print palindrome_permutation("are we not drawn onward to new era")
print palindrome_permutation("the city")