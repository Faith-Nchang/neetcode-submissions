class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1 for _ in range(len(nums))]
        suffix_mult = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefix_mult[i] = prefix_mult[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                suffix_mult[i] = suffix_mult[i+1] * nums[i+1]
        
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix_mult[i] * suffix_mult[i]
        return res


