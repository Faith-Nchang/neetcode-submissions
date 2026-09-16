class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]
        for ch in tokens:
            if ch in operators:
                right = stack.pop()
                left = stack.pop()
                if ch == "+":
                    val = left + right
                elif ch == "-":
                    val = left - right
                elif ch == "*":
                    val = left * right
                else:
                    val = int(left / right)
                
                stack.append(val)
            else:
                stack.append(int(ch))

        return stack.pop() if stack else 0




        