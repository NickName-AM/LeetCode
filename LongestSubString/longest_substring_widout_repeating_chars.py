class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        highestLength = 0
        a = ''
        i = 0
        if len(s) == 1:
            return 1

        # Starting for the ith index, get every possible substring
        # and stop when character repeats
        while i< len(s):
            j = i
            while j<len(s):
                if s[j] in a:
                    
                    if highestLength < len(a):
                        highestLength = len(a)
                    a = ''
                    break
                else:
                    a += s[j]
                j+=1
            i+=1

        return highestLength

# Tests
print(
Solution().lengthOfLongestSubstring("abcabcbb"),
Solution().lengthOfLongestSubstring("bbbbb"),
Solution().lengthOfLongestSubstring("pwwkew")
)