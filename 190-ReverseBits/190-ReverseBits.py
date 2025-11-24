# Last updated: 24/11/2025, 17:26:51
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << 31 - i)
        return result