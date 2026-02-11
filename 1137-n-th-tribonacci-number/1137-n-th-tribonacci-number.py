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
        return top_down(n)