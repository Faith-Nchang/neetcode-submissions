class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        for ch in s:
            if ch not in l1:
                l1[ch] = 0
            l1[ch] += 1

        l2 = {}
        for ch in t:
            if ch not in l2:
                l2[ch] = 0
            l2[ch] += 1

        for ch, freq in l1.items():
            if ch not in l2 or l2[ch] != freq:
                return False
        return len(l1) == len(l2)


       
        