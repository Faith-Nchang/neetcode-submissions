from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numset = set(nums)
        max_seq = 0


        for num in nums:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1

                max_seq = max(max_seq, length)
        return max_seq
