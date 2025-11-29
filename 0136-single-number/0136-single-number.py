class Solution:
    def singleNumber(self, nums):
        xored = nums[0]
        for i in range(len(nums)-1):
            xored ^= nums[i+1]
        return xored