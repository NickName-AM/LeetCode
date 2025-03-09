class Solution:
    def sortedSquares(self, nums):
        n = len(nums)

        l, r = 0, n - 1

        sq = [0] * n

        for i in range(n-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                val = nums[l]
                l += 1
            else:
                val = nums[r]
                r-=1
            
            sq[i] = val**2


        return sq

a = Solution().sortedSquares
print(a([-4,-1,0,3,10]))
print(a([-7,-3,2,3,11]))