class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_1 = {}
        for c in s:
            freq_1[c] = freq_1.get(c, 0) + 1

        freq_2 = {}
        for c in t:
            freq_2[c] = freq_2.get(c, 0) + 1

        for c in freq_1:   
            if c not in freq_2 or freq_1[c] != freq_2[c]:
                return False
                
        return len(freq_1) == len(freq_2)
        