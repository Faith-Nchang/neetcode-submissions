class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        def helper(index, comb, total):

            if total == target:
                combinations.append(comb.copy())
                return
            elif index >= len(nums) or total > target:
                return

            # back tracking part
            comb.append(nums[index])
            helper(index, comb, total + nums[index])

            comb.pop()
            helper(index + 1, comb, total)

        helper(0, [], 0)

        return combinations
        