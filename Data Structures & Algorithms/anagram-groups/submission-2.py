from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = defaultdict(list)

        for word in strs:
            s = str(sorted(word))
            buckets[s].append(word)

        return list(buckets.values())
        