class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        if x == 0 or x == 1:
            return x
        while l<r:
            mid = (l+r)//2
            if r==l+1:
                return l
            elif mid*mid > x:
                r = mid
            elif mid*mid < x:
                l = mid
            else:
                return mid