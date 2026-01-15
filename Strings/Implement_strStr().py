"Return the index of the first occurrence of needle in haystack, or -1 if not found.
Example
Input: haystack = "hello", needle = "ll"
Output: 2
"

def strStr(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1
