class Solution:
    def mySqrt(self, x: int) -> int:
        #Using BS
        l = 0 
        r = x
        res = 0
        
        while l <= r:
            mid = l + (r-l ) // 2
            sq = mid * mid 
            if sq > x:
                r = mid - 1
            elif sq < x:
                l = mid + 1
                res = mid
            else:
                return mid

        return res