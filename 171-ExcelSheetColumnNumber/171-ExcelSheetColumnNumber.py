# Last updated: 24/11/2025, 17:26:53
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result += 26**i * (ord(columnTitle[-(i+1)]) - 64)
        return result