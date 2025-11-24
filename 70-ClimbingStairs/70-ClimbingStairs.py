# Last updated: 24/11/2025, 17:27:15
class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        f1 = 0
        f2 = 1
        counter = 0
        while counter < n:
            sum = f1 + f2
            f1 = f2
            f2 = sum
            counter += 1
        return sum