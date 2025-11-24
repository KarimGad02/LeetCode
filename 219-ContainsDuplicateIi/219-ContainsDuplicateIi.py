# Last updated: 24/11/2025, 17:26:44
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for index, num in enumerate(nums):
            if num in seen:
                if abs(seen[num] - index) <= k:
                    return True
            seen[num] = index
        return False