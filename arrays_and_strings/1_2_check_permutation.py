# 1.2 Check Permutation
# ==============================================================================================
# Given two strings, write a method to decide if one is a permutation of the other
# ==============================================================================================
def check_permutation(s1, s2):
	char_counts = [0] * 128 # assume ASCII
	for char in s1:
		char_counts[ord(char)] += 1
	for char in s2:
		char_counts[ord(char)] -= 1
	for char in char_counts:
		if char > 0:
			return False
	return True

print check_permutation("diana", "danai")