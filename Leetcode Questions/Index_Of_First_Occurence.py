def strStr(haystack, needle):
    if not needle:
        return 0
    len_haystack = len(haystack)
    len_needle = len(needle)
    for i in range(len_haystack - len_needle + 1):
        # print(haystack[i])
        print(haystack[i: i + len_needle])
        if haystack[i: i + len_needle] == needle:
            # print(haystack[i: i + len_needle])
            return i
    return -1

haystack = "helloworld"
needle = "low"
# strStr(haystack, needle)
# print(strStr(haystack, needle))


def index_of_first_occurence(needle, haystack):
    # if needle is an empty string then return 0
    
    if not needle:
        return 0
    len_needle, len_haystack = len(needle), len(haystack)
    # loop through haystack but only till there is enough chars to compare in needle
    for i in range(len(haystack) - len(needle) + 1):
        print(haystack[i])
        # check from index i to len(needle) and compare with haystack and return i if true
        if haystack[i: i + len_needle] == needle:
            return i
    return -1


haystack = "helloworld"
needle = "low"
print(index_of_first_occurence(needle, haystack))
