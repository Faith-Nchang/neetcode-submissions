from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        t_map = Counter(t)

        min_subs = ""
        min_size = float("inf")

        l = 0

        subs_freq = {}
        have, need = 0, len(t_map)

        for r in range(len(s)):
            ch = s[r]
            subs_freq[ch] = subs_freq.get(ch, 0) + 1

            if ch in t_map and subs_freq[ch] == t_map[ch]:
                have += 1

            # shrink the window
            while have == need:
                window_size = r - l + 1
                if window_size < min_size:
                    min_size = window_size
                    min_subs = s[l:r + 1]
                c = s[l]
                subs_freq[c] -= 1
                if c in t_map and subs_freq[c] < t_map[c]:
                    have -= 1
                l+=1


            

        return min_subs

        




        