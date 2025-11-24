# Last updated: 24/11/2025, 17:26:54
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate