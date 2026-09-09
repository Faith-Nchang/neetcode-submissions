class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_freq = {}

        max_f = 0
        l = 0
        max_window = 0

        for r in range(len(s)):
            char_freq[s[r]] = 1 + char_freq.get(s[r], 0)

            if char_freq[s[r]] > max_f:
                max_f = char_freq[s[r]]
            
            # shrink the window
            while (r - l + 1) - max_f > k:
                char_freq[s[l]] -= 1
                l += 1
            
            max_window = max(max_window, r - l + 1)

        return max_window

            

        