class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            #if len(stack) > 0: print(stack[-1])
            if ch == ')' and (len(stack) > 0 and stack[-1]=='('):
                stack.pop()
            elif ch == '}' and (len(stack) > 0 and stack[-1]=='{'):
                stack.pop()
            elif ch == ']' and (len(stack) > 0 and stack[-1]=='['):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)==0