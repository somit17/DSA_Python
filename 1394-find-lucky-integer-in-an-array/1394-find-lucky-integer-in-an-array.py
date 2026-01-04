class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        max_val =-1
        for num in arr:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1

        for key,value in dic.items():
        #print(f"K - {key} -- > {value}")
            if key==value and value > max_val:
                max_val = value

        return max_val