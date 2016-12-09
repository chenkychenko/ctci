# 8.9 Parens
# ==============================================================================================
# Implement an algorithm to print all valid (ie, properly opened and closed) combinations of n
# pairs of parentheses.
# ==============================================================================================
def parens(num_pairs):
    if num_pairs == 0:
        results = []
        results.append([''])
        return results
    results = parens(num_pairs - 1)
    # print "Results: {}".format(results)
    more = []
    for i in results:
        new_res = insert_into_gaps(i)
        more += new_res
    more.append(get_base_combo(num_pairs))
    return more


def insert_into_gaps(combo):
    results = []
    for i, val in enumerate(combo):
        if val == '(':  # open paren, insert
            new_val = combo[:]
            new_val.insert(i + 1, '(')
            new_val.insert(i + 2, ')')
            results.append(new_val)
    return results


def get_base_combo(num):
    res = []
    for i in range(num):
        res.append('(')
        res.append(')')
    return res


print "\n\n\nPARENS:"
paren = ['(', ')', '(', ')']
res = insert_into_gaps(paren)
print res

print get_base_combo(5)

print "\n\n\nRESULTS!"

results = parens(3)
for res in results:
    print ''.join(res)