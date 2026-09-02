class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

       

        left = self.dfs(nums[:-1])
        right = self.dfs(nums[1:])
        return max(left, right, nums[0])

        
    def dfs(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
