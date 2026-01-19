class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = set()
        k=0
        for num in nums:
            if num not in unique:
                unique.add(num) 
                nums[k]=num
                k+=1

        return k