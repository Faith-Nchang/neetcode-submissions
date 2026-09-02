class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nS = set(nums)

        maxL= float('-inf')

        for n in nums:
            if n - 1 not in nS:
                length = 1

                while n + length in nS:
                    length += 1
                maxL = max(maxL, length)
        return maxL

