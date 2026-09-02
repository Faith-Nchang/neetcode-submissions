class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        freq_map = {}

        l = 0

        maxF = 0
        for r in range(len(s)):
            # get the freq of the max char
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            maxF = max(maxF, freq_map[s[r]])

            while (r - l + 1) - maxF > k:
                freq_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        

            
        return res