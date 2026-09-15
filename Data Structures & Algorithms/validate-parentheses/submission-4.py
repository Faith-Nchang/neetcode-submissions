class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']':'['}

        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack or stack.pop() != char_map[ch]:
                    return False
        return len(stack) == 0

        