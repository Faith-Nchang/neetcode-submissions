from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = Counter(s1)
        window_freq = {}
        l = 0
        for r in range(len(s2)):
            ch = s2[r]
            window_freq[ch] = window_freq.get(ch, 0) + 1

            while l <= r and (r - l + 1) > len(s1):   
                window_freq[s2[l]] -= 1

                if window_freq[s2[l]] == 0:
                    del window_freq[s2[l]]

                l += 1
          
            if s1_freq  == window_freq:
                return True

        return False