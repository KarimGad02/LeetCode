class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = 0
        decimal_b = 0
        power_a = len(a) - 1
        power_b = len(b) - 1
        for digit in a:
            decimal_a += int(digit) * (2 ** power_a)
            power_a -= 1
        for digit in b:
            decimal_b += int(digit) * (2 ** power_b)
            power_b -= 1
        decimal_sum=decimal_b+decimal_a
        binary_sum = ""
        while decimal_sum > 0:
            remainder = decimal_sum % 2
            binary_sum = str(remainder) + binary_sum
            decimal_sum //= 2
        return binary_sum if binary_sum else "0"