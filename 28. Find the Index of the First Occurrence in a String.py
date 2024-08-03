def strStr(haystack: str, needle: str) -> int:

    # If the needle is empty, return 0 (as per common convention)
    if len(needle) == 0:
        return 0

    # If the haystack is shorter than the needle, it's impossible for needle to be in haystack.
    if len(haystack) < len(needle):
        return -1

    # Loop through the haystack, but stop len(needle) characters before the end to avoid out-of-bounds error.
    for i in range(len(haystack) - len(needle) + 1):
        # Check if the substring of haystack starting at i and of length len(needle) matches needle.
        if haystack[i:i+len(needle)] == needle:
            # haystack[0:3]
            # haystack: [0, 1, 2]
            return i  # Return the index if a match is found.

    return -1  # Return -1 if no match is found.


print(strStr("abcdefg", "efg"))

