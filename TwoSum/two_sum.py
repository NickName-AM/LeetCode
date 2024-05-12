class Solution(object):
    def twoSum(self, nums, target):
        res = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                r = nums[i] + nums[j]
                if r == target:
                    res += [i, j]
                    return res
                j+=1
            i+=1


Solution().twoSum(nums=[2, 7, 11, 15], target=9)
Solution().twoSum(nums=[3, 2, 4], target=6)
Solution().twoSum(nums=[3, 3], target=6)
