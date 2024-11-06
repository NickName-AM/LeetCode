class Solution:
    def longestPalindrome(self, s: str) -> str:

        substring = ""

        i = 0
        while i < len(s):
            j = len(s) - 1
            while j >= i:
                if s[i] != s[j]:
                    j-=1
                    continue
                else:
                    sub = s[i:j+1]
                    if (sub == sub[::-1]) and (len(substring) < len(sub)):
                        substring = sub
                j-=1
            i+=1
        
        return substring

print(Solution().longestPalindrome("aacabdkacaa"))