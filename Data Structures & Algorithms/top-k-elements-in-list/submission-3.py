from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, f in freq.items():
            buckets[f].append(n)


        res = []

        for i in range(len(buckets) - 1 , -1, -1):
            elts = buckets[i]
            for elt in elts:

                res.append(elt)
                if len(res) == k:
                    return res

        