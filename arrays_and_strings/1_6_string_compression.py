# 1.6 String Compression
# ==============================================================================================
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the original string. You can
# assume the string has only uppercase and lowercase letters (a-z).
# ==============================================================================================
def string_compression(s):
    compressed = []
    count = 0
    for i in range(len(s)):
        count += 1
        if (i+1) == len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0
    return ''.join(compressed) if len(compressed) < len(s) else ''.join(s)

print string_compression("aaaabbbcccdd")