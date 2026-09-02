class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in kv:
                return [kv[c], i]
            
            kv[nums[i]] = i
        return []
        