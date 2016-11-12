# 1.5 One Away
# ==============================================================================================
# There are three types of edits that can be performed on strings: insert a character, remove a
# character or replace a character. Given two strings, write a function to check if they are one
# edit (or zero edits) away.
# ==============================================================================================
def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) == len(s2): # same length, must be replace
        return check_replace(s1, s2)
    longer = s1 if len(s1) > len(s2) else s2
    shorter = s2 if len(s1) > len(s2) else s1
    return check_insert(shorter, longer)

def check_replace(s1, s2):
    found_replacement = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_replacement:
                return False
            found_replacement = True
    return True

def check_insert(s1, s2):
    found_insert = False
    j = 0
    for i in range(len(s1)):
        if s1[i] != s2[j]:
            if found_insert:
                return False
            found_insert = True
            j += 1
        j += 1
    return True

print one_away("pale", "ple")
print one_away("pales", "pale")
print one_away("pale", "bale")
print one_away("pale", "bake")