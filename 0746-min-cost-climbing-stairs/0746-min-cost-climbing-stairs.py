class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Bottom Up Approach
        def bottom_up(cost) -> int:
            n = len(cost)
            prev_1 = cost[1]
            prev_2 = cost[0]
            if n == 0:return prev_2
            if n == 1:return prev_1

            for i in range(2,n):
                current = min(prev_1,prev_2) + cost[i]
                prev_2 = prev_1
                prev_1 = current

            return min(prev_1,prev_2)
        return bottom_up(cost)