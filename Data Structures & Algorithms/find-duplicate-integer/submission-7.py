class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            i = num 
            if num < 0:
                i *= -1

            if nums[i] < 0:
                return max(num, num * -1)
            
            nums[i] *= -1
        