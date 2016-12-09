# 8.7 Permutations without Dups
# ==============================================================================================
# Write a method to compute all permutations for a string of unique chatacters.
# ==============================================================================================
def get_permutations(word, perms=None):
    if not word or len(word) == 1:
        return word # we are done
    if not perms:
        first_letter = word.pop()
        perms = [[first_letter]]
    letter = word.pop()
    new_perms = []
    for p in perms:
        solutions = insert_in_every_position(letter, p)
        new_perms.extend(solutions)
    return get_permutations(word, new_perms)

def insert_in_every_position(letter, permutation):
    solutions = []
    for i in range(len(permutation)+1):
        print "inserting {} into index {}".format(letter, i)
        modified_word = permutation[:]
        modified_word.insert(i, letter)
        solutions.append(modified_word)
    print "SOLUTIONS: {}".format(solutions)
    return solutions

print "\n\n~~~~~~PERMUTATIONS~~~~~\n\n"
result = get_permutations(list("a"))
print result
print "length: {}".format(len(result))

def get_perms(remainder):
    print "REMAINDER: {}".format(remainder)
    result = []
    if len(remainder) == 0:
        result.append("")
        print "BASE CASE RESULT: {}".format(result)
        return result # we are done, base case!
    for i in range(len(remainder)):
        without_i = remainder[:]
        without_i.pop(i)
        partials = get_perms(without_i)
        print "PARTIALS: {}".format(partials)
        for s in partials:
            result.append(remainder[i] + s)
    # print "RESULT: {}".format(result)
    return result

print "\n\n\n permutations the other way:\n\n\n"
res = get_perms(list('abc'))
print res

def get_perms2(prefix, remainder, result):
    if not remainder: # base case
        result.append(prefix)
    else:
        for i in range(len(remainder)):
            before = remainder[:i]
            after = remainder[i+1:]
            letter = remainder[i]
            get_perms2(prefix + letter, before + after, result)

def perms_helper2(word):
    results = []
    get_perms2('', list(word), results)
    return results

res = perms_helper2('abc')
print res