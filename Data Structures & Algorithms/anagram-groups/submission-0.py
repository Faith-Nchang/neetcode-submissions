class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        def isAnagram(s1, s2):

            freq1 = {}

            for c in s1:
                freq1[c] = freq1.get(c, 0) + 1
            freq2 = {}

            for c in s2:
                freq2[c] = freq2.get(c, 0) + 1

            for c in freq1:
                if c not in freq2 or freq1[c] != freq2[c]:
                    return False
            return len(freq1) == len(freq2)
        
        for word in strs:
            added = False

            for s in anagrams:
                if isAnagram(word, s):
                    anagrams[s].append(word)
                    added = True
                    break
            if not added:
                anagrams[word] = [word]
        
        final_anagrams = []
        for w in anagrams:
            final_anagrams.append(anagrams[w])

        return final_anagrams

            
        