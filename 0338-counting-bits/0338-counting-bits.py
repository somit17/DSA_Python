class Solution:
    def countBits(self, n: int) -> List[int]:
        #Hamming Weight
        def hamming_weight(num):
            count = 0
            while num:
                num &= (num -1)
                count+=1
            return count
        result = []
        for i in range(0,n+1):
            result.append(hamming_weight(i))
        return result