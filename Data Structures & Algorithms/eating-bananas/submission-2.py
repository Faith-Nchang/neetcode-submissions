import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p = max(piles)

        min_k = float('inf')
        l, r = 1, max_p 

        while l <= r:
            k = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)

            if hrs <= h:
                min_k = min(k, min_k)
                r = k - 1
            else:
                l = k + 1  
                
        return min_k


        