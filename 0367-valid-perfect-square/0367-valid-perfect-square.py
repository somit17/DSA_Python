class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Using Binary Search approach

        for i in range(1,num+1):
            sq = i * i
            if sq > num:
                return False
            if sq == num:
                return True
        