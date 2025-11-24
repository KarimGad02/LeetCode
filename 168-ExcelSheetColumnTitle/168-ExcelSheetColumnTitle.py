# Last updated: 24/11/2025, 17:26:55
class Solution:
    def convertToTitle(self, columnNumber):
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            columnNumber = columnNumber // 26
        return result
