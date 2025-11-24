# Last updated: 24/11/2025, 17:26:52
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1 if (n & 1) else 0
            n >>= 1
        return count