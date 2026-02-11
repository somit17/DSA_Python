class Solution:
    def climbStairs(self, n: int) -> int:
        #Top-Down Approach
        #Memoisation

        memo = {}
        def top_down_approach(n) -> int:
            if n in memo:
                return memo[n]
            #Base Cases
            if n == 1 : return 1
            if n == 2 : return 2
            result = top_down_approach(n-1) + top_down_approach(n-2)
            memo[n] = result
            return result


        #Bottom Up Approach
        def bottom_up_approach(n) -> int:
            #Base case because if num are 1 or 2 index error
            if n == 1: return 1
            if n == 2: return 2
            ways = [0] * (n+1) #Init
            ways[1] = 1
            ways[2] = 2

            for i in range(3,n+1):
                ways[i] = ways[i-1]+ways[i-2]

            return ways[n]
        
        return bottom_up_approach(n)
        