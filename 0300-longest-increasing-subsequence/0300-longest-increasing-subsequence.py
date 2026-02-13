class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n  # each element is a subsequence of length 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)