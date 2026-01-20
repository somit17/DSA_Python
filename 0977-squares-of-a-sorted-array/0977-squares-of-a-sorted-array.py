class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [num ** 2 for num in nums]

        #Two pointers
        n = len(result)
        l,r,write_index = 0,n-1,n-1
        output = [0] * n


        while l<=r:
            l_sq = result[l]
            r_sq = result[r]
            if l_sq > r_sq:
                output[write_index]=l_sq
                l+=1
            else:
                output[write_index]=r_sq
                r-=1
            write_index-=1

        return output 