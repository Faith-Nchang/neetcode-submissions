from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)

        for ch, freq in freq_s.items():
            if ch not in freq_t or freq_t[ch] != freq:
                return False
        return len(freq_s) == len(freq_t)
        