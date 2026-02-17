class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows < 1:
            return result
        
        #Add 1 at start
        current = [1]
        result.append(current)

        for i in range(2,numRows + 1):
            prev = 0
            temp_list = []
            for num in current:
                new_val = prev + num
                temp_list.append(new_val)
                prev = num 
            temp_list.append(1) #Add 1 at last
            result.append(temp_list)
            current = temp_list
            
        return result