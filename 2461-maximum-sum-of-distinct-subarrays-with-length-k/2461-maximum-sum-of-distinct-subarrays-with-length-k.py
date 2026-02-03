from typing import List
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        #Track freq of elements
        freq = defaultdict(int)
        window_sum = 0

        #Initialize window
        for i in range(k):
            freq[nums[i]]+=1
            window_sum+=nums[i]

        # Check if first window has all distinct elements
        max_sum = window_sum if len(freq) == k else 0


        #Slide window
        for i in range(k,n):
            #Remove leftmost element 
            left_num = nums[i-k]
            freq[left_num]-=1
            if freq[left_num]==0:
                del freq[left_num]
            window_sum -= left_num

            #Add rightmost
            right_num = nums[i]
            freq[right_num] +=1
            window_sum +=right_num

            #Check if current window has all distince elements
            if len(freq) == k:
                max_sum = max(max_sum,window_sum)
        
        return max_sum