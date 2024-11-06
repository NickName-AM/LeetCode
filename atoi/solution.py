class Solution:
    def myAtoi(self, s: str) -> int:
    
        s = s.strip()

        if s == "":
            return 0

        t = ''

        if s[0] == '-':
            t += '-'
        else:
            t += '+'
            if s[0] != '+':
                s = '+' + s

        i = 1
        while i < len(s) and s[i].isdigit():
            if s[i] == '0' and len(t) == 1:
                i+=1
                continue
            
            t += s[i]
            i += 1
        
        if len(t) == 1:
            t += '0'
        
        t = int(t)

        if t < -2**31:
            t = -2**31
        elif t > 2**31 - 1:
            t = 2**31 - 1
        
        return t


print(Solution().myAtoi("words and 987"))
            


        
        