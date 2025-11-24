# Last updated: 24/11/2025, 17:26:50
class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        while n != 1 and n not in memory:
            memory.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1