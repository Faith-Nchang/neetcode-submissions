from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = defaultdict(list)

        # for word in strs:
        #     s = str(sorted(word))
        #     buckets[s].append(word)

        # return list(buckets.values())

        for word in strs:
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1

            buckets[tuple(key)].append(word)
        return list(buckets.values())