# 1.3 URLify
# ==============================================================================================
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the 
# "true" length of the string.
# ==============================================================================================
def urlify(word, true_len):
    word = list(word)
    space_count = 0
    for i in range(true_len):
        if word[i] == " ":
            space_count += 1
    print "spaces: {}".format(space_count)
    expanded_length = true_len + space_count * 2
    print "expanded length is: {}".format(expanded_length)
    j = expanded_length - 1
    for i in range(true_len-1, 0, -1): # start from the back
        if word[i] != " ":
            word[j] = word[i]
            j -= 1
        else:
            word[j] = '0'
            word[j-1] = '2'
            word[j-2] = '%'
            j -= 3
    return word

print urlify("Mr John Smith               ", 13)