from typing import List


class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
# the reason to sort the list, it's because it's the first one have it, the one must have the same letter as well.
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return f"there is no common prefix {ans}"
            ans += first[i]
        return ans


# Example usage:
v = ["flower","flow","flight"]


solution = Solution()
print(solution.longestCommonPrefix(v))  # Output: "fl"
