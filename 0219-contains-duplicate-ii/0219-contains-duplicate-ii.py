class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Sliding Window Solution by template
        if k == 0:
            return False

        n = len(nums)
        size = k+1
        #Check if array is smaller than window
        if size >= n:
            return len(set(nums)) != n #Will return true if duplicates

        window_set = set(nums[:size])

        #IF window has duplicates
        if len(window_set) != size:
            return True

        for i in range(size,n):
            left_most = window_set.remove(nums[i-size])

            if nums[i] in window_set:
                return True

            window_set.add(nums[i])
        return False
        