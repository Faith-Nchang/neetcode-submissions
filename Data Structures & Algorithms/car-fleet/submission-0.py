class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[pos, s] for pos, s in zip(position, speed)] 
        
        for p, s in sorted(pairs)[::-1]:
            arrival = (target - p) / s
            stack.append(arrival)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    