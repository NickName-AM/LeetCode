from unittest import TestCase

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

        strs.sort()

        first = strs[0]
        last = strs[-1]

        prefix = ""

        for i in range(0, min([len(first), len(last)])):
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        
        return prefix

# Tests
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
