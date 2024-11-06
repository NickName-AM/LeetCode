class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

        commons = ""

        smallest = min(strs, key=len)
        i = 0
        

        while i < len(smallest):
            j = 0
            c = 0
            char = smallest[i]

            while j < len(strs):
                if strs[j][i] == char:
                    c+=1
                else:
                    break

                j+=1
                
            if c == len(strs):
                commons += char
            else:
                break
            
            i+=1
        
        return commons
                


print(Solution().longestCommonPrefix(["dog","racecar","car"]))