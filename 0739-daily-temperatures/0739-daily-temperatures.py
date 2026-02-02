class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonous stack problem
            #we need to indentify next greater element so Monotonously decreasing
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if len(stack)==0:
                result[i]=0
            else:
                result[i] = stack[-1]-i # days until warmer temperature
            stack.append(i)
        return result