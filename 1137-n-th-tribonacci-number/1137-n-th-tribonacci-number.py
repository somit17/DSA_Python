class Solution:
    def tribonacci(self, n: int) -> int:
        #Top-Down
        memo = {}
        def top_down(n) -> int:
            if n in memo:
                return memo[n]
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1

            result = top_down(n-1)+top_down(n-2)+top_down(n-3)
            memo[n]=result
            return memo[n]

        #Bottom-Up
        def bottom_up(n) -> int:
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1
            result = [0] * (n+1)
            result[0] = 0
            result[1] = 1
            result[2] = 1

            for i in range(3,n+1):
                result[i] = result[i-1]+result[i-2]+result[i-3]

            return result[n]

        return bottom_up(n)