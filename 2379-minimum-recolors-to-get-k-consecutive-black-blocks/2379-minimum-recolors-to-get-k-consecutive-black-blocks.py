class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #Sliding window

        n = len(blocks)
        white_count = blocks[:k].count('W')
        min_ops = white_count

        for i in range(k,n):
            if blocks[i-k] == 'W':
                white_count-=1
            if blocks[i] == 'W':
                white_count+=1
            
            min_ops = min(white_count,min_ops)

        return min_ops
        