# Last updated: 24/11/2025, 17:26:43
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if(len(unique) == len(nums)):
            return False
        return True