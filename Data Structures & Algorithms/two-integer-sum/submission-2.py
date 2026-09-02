class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in f:
                return [f[comp], i] 
            f[nums[i]] = i
        return []

