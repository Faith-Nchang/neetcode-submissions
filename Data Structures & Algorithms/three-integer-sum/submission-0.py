from collections import defaultdict
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos_sums = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pos_sums[nums[i] + nums[j]].append([i, j])  

        res = set()
        for k in range(len(nums)):
            target = -nums[k]
            if target in pos_sums:
                for i, j in pos_sums[target]:
                    if k != i and k != j:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)
        return list(res)
