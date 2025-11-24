# Last updated: 24/11/2025, 17:27:00
class Solution:
    def singleNumber(self, nums):
        xored = nums[0]
        for i in range(len(nums)-1):
            xored ^= nums[i+1]
        return xored