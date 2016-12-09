# 8.8 Permutations with Dups
# ==============================================================================================
# Write a method to compute all permutations for a string whose characters are not necessarily
# unique. The list of permutations should not have duplicates.
# ==============================================================================================
def get_perms(word):
    char_map = build_freq_table(word)
    results = []
    get_perms_dups(char_map, '', len(word), results)
    return results

def build_freq_table(word):
    char_map = {}
    for char in word:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1
    return char_map

def get_perms_dups(char_map, prefix, rem, results):
    if not rem:
        results.append("")
        return
    for c in char_map:
        count = char_map.get(c)
        if count > 0:
            char_map[c] = count - 1
            get_perms_dups(char_map, prefix + c, rem - 1, results)
            char_map[c] = count