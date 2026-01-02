class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        length = len(nums)
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] == length // 2:
                return num

        return -1