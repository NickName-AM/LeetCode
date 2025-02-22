class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()

        r = []

        l = len(nums)

        for i in range(0, l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = l - 1   # last index

            while j < k:
                
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j+=1
                elif sum > 0:
                    k-=1
                else:
                    r.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
        
        return r


# Tests
Result = Solution().threeSum

print(Result([-1,0,1,2,-1,-4]))
print(Result([0,1,1]))
print(Result([0,0,0]))

