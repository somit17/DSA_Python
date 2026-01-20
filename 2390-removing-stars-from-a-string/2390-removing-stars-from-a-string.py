class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                if stack and len(stack) > 0:
                    stack.pop()
            else :
                stack.append(ch)

        return "".join(stack)