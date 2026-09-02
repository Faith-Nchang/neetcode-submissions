class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openS = {'[': ']', '{': '}', '(':')'}

        for c in s:
            if c in openS:
                stack.append(c)
            elif stack:
                compl = stack.pop()
                if openS[compl] != c:
                    return False
            else:
                return False
        return len(stack) == 0


            
        