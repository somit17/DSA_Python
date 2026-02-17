from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num]+=1
            if my_dict[num] > n // 2:
                return num
        return -1
        