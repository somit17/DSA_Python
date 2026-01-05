class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for data in details:
            age = str(data[-4])+str(data[-3])
            if int(age) > 60:
                count+=1
        

        return count